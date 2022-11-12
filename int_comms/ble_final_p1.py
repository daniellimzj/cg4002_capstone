import multiprocessing as mp
import os
import queue
import struct
import sys
import time
from socket import *

import MQTT
import paho.mqtt.client as mqtt
import sshtunnel
from bluepy.btle import DefaultDelegate, Peripheral

INDEX_GUN_P1 = 2
INDEX_GUN_P2 = 5

TIMEOUT_NOTIFICATION = 2 #s
TIMEOUT_HANDSHAKE = 50/100 #s

TIME_DATA_RATE_COUNT = 60 #s

btleAddrs = [
    "D0:39:72:BF:CA:CF", # P1 Arm
    "D0:39:72:BF:C8:A6", # P1 Vest 
    "D0:39:72:BF:CA:FC", # P1 Gun 
    "D0:39:72:BF:CA:A6", # P2 Arm
    "D0:39:72:BF:CA:81", # P2 Vest 
    "D0:39:72:BF:CA:FA"  # P2 Gun 
]

btleHandshakes = [False] * 6

class ChecksumError(Exception):
    pass

class Comms(DefaultDelegate):
    def __init__(self, serialChar, index, clientSocket):
        DefaultDelegate.__init__(self)
        self.serialChar = serialChar
        self.index = index
        self.clientSocket = clientSocket
        self.buffer = b''
        self.fragmented = 0
        self.dropped = 0

    def sendAckPacket(self):
        self.serialChar.write(bytes("A", "utf-8"))

    def handleAckPacket(self):
        self.sendAckPacket()
        btleHandshakes[self.index] = True

    def handleGunAndVestPacket(self, data):
        self.clientSocket.send(data)
        self.sendAckPacket()


    def handleArmPacket(self, data):
        # Packet Indexing:
        # 0 - Packet Type
        # 1 - Mean
        # 2 - Range
        # 3 - Variance
        # 4 - Median
        # 5 - Shoots Gun
        # 6 - Gets Shot

        self.clientSocket.send(data)
        self.sendAckPacket()

    def verifyChecksum(self, data):
        packetBytes = struct.unpack('<20b', data)
        sum = 0
        count = 0
        byte = 0

        for byte in packetBytes:
            if count == 19:
                if sum == byte:
                    return True
                else:
                    break

            sum ^= byte
            count += 1

        return False

    def handleFragmentation(self, data):
        self.buffer = self.buffer + data
        self.fragmented += 1
        if len(self.buffer) == 20: 
            self.handleNotification(None, self.buffer)
            self.buffer = b''

    def handleChecksumError(self, data):
        currBuffer = len(self.buffer)
        currData = data[:(20-currBuffer)]
        self.buffer = self.buffer + currData
        self.handleNotification(None, self.buffer)
        self.buffer = data[(20-currBuffer):]

    def handleNotification(self, charHandle, data):
        try:
            packet = ()
            packetFormat = (
                '<b'  # Packet Type
                'h'   # accX
                'h'   # accY
                'h'   # accZ
                'h'   # gyroX
                'h'   # gyroY
                'h'   # gyroZ
                'f'   # padding
                '?'   # Gun is Shot
                '?'   # Got Shot
                'b'   # Checksum
            )
            packet = struct.unpack_from(packetFormat, data, 0)
            if len(packet) == 11:
                if not self.verifyChecksum(data):
                    raise ChecksumError("Incorrect checksum")

            packetType = packet[0]
            # P1: D, G, V       P2: E, J, W
            if packetType == ord('D') or packetType == ord('E'):
                self.handleArmPacket(data)
            elif packetType == ord('G') or packetType == ord('J') or packetType == ord('V') or packetType == ord('W'):
                self.handleGunAndVestPacket(data)
            elif packetType == ord('A'):
                self.handleAckPacket()

        except struct.error:
            self.handleFragmentation(data)

        except ChecksumError:
            if (len(self.buffer) != 0):
                self.handleChecksumError(data)

        except Exception as e:
            self.dropped += 1
            pass

def startMQTTClient(id: int, queue: mp.Queue):

    def on_connect(client: mqtt.Client, userdata, flags, rc):
        print("Connected with result code " + str(rc))

        if id == 1:
            client.subscribe(MQTT.Topics.didP1Reload)
        elif id == 2:
            client.subscribe(MQTT.Topics.didP2Reload)

    def on_message(client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))
        queue.put(bool(int(msg.payload)))

    try:
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect(MQTT.Configs.broker, MQTT.Configs.portNum)
        client.loop_forever()

    finally:
        print("disconnecting player", id, "client...")
        client.disconnect()

def initHandshake(beetle, serialChar, index):
    while not btleHandshakes[index]:
        serialChar.write(bytes("H", "utf-8"))

        if beetle.waitForNotifications(TIMEOUT_HANDSHAKE):
            pass

def checkReload(serialChar, mqttQueue):
    try:
        didPlayerReload = mqttQueue.get(block=False, timeout=None)
        print("did player reload:", didPlayerReload)
        if didPlayerReload == 1:
            serialChar.write(bytes("R", "utf-8"))
    except queue.Empty:
        pass

def watchForDisconnect(beetle, index):
    while True:
        if not beetle.waitForNotifications(TIMEOUT_NOTIFICATION):
            break

    print("No data for 2 seconds, attempting to reconnect...")
    btleHandshakes[index] = False
    beetle.disconnect()  # Disconnects first and try to reconnect again
    return True

def watchForDisconnectGun(beetle, index, serialChar, mqttQueue):
    while True:
        if not beetle.waitForNotifications(TIMEOUT_NOTIFICATION):
            print("breaking loop")
            break
        checkReload(serialChar, mqttQueue)
        
    print("No data for 2 seconds, attempting to reconnect...")
    btleHandshakes[index] = False
    beetle.disconnect()  # Disconnects first and try to reconnect again
    return True

def beetleProcess(index, beetlePort): 
    addr = btleAddrs[index]
    serialSvc = None
    serialChar = None
    beetle = Peripheral()
    notStop = True

    # Starts MQTT Client for Gun Beetle
    if (index == INDEX_GUN_P1 or index == INDEX_GUN_P2): 
        print("in here")
        mqttQueue = mp.Queue()
        mqttClientProcess = mp.Process(target = startMQTTClient, args=(1, mqttQueue))
        mqttClientProcess.start()
        print("mqtt client started for beetle", index)
        time.sleep(0.5)

    try:
        with sshtunnel.open_tunnel(
            'sunfire.comp.nus.edu.sg',
            ssh_username="danielim",
            ssh_password="Cg4002!",
            remote_bind_address=('192.168.95.234', beetlePort),
        ) as tunnel:

            serverName = 'localhost'
            serverPort = int(tunnel.local_bind_port)
            clientSocket = socket(AF_INET, SOCK_STREAM)
            clientSocket.connect((serverName, serverPort))
            print("connected to:", serverName, serverPort)

            while notStop:
                try:
                    print("Searching for Beetle", str(index))
                    beetle.connect(addr)
                    print("Connecting to Beetle {0}...".format(index))

                    serialSvc = beetle.getServiceByUUID(
                        "0000dfb0-0000-1000-8000-00805f9b34fb")
                    serialChar = serialSvc.getCharacteristics(
                        "0000dfb1-0000-1000-8000-00805f9b34fb")[0]
                    delegate = Comms(serialChar, index, clientSocket)
                    beetle.withDelegate(delegate)

                    if not btleHandshakes[index]:
                        initHandshake(beetle, serialChar, index)
                        print("Beetle " + str(index) +": Handshake Successful!")
                        print("Beetle {0} Handshake Status: {1}".format(index, btleHandshakes[index]))

                    if btleHandshakes[index]:
                        if (index == INDEX_GUN_P1 or index == INDEX_GUN_P2):
                            notStop = watchForDisconnectGun(beetle, index, serialChar, mqttQueue)
                        else:
                            notStop = watchForDisconnect(beetle, index)

                except KeyboardInterrupt:
                    beetle.disconnect()
                except Exception as e:
                    pass
    except KeyboardInterrupt:
        if (index == INDEX_GUN_P1 or index == INDEX_GUN_P2):
            mqttClientProcess.terminate()
    finally:
        if (index == INDEX_GUN_P1 or index == INDEX_GUN_P2):
            mqttClientProcess.join()    


if __name__ == "__main__":

    _num_param = 2
    if len(sys.argv) < _num_param:
        print("Invalid number of arguments!")
        print("python3 " + os.path.basename(__file__) + " [Beetle Port]")
        print("Beetle Port: Port number of beetle")
        sys.exit()
    beetlePort = int(sys.argv[-1])
    print("Beetle Port:", beetlePort)
    beetle0Process = mp.Process(target=beetleProcess, args=(0, beetlePort))
    beetle1Process = mp.Process(target=beetleProcess, args=(1, beetlePort))
    beetle2Process = mp.Process(target=beetleProcess, args=(2, beetlePort))

    try:
        beetle0Process.start()
        beetle1Process.start()
        beetle2Process.start()

        beetle0Process.join()
        beetle1Process.join()
        beetle2Process.join()
    finally:
        beetle0Process.terminate()
        beetle1Process.terminate()
        beetle2Process.terminate()

        print("Closing main")
