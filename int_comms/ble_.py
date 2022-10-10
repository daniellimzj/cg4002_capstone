import struct
import multiprocessing as mp
import time

from bluepy.btle import Peripheral, DefaultDelegate

import json
from socket import *

import sshtunnel
# from ext_comms.BeetleMain import BEETLE_PORT
BEETLE_PORT = 6721

TIMEOUT_NOTIFICATION = 2 #s
TIMEOUT_HANDSHAKE = 50/100 #s

TIME_DATA_RATE_COUNT = 60 #s

btleAddrs = [
    "D0:39:72:BF:CA:CF", # btleArm0
    "D0:39:72:BF:C8:A6", # btleVest0
    "D0:39:72:BF:CA:FC", # btleGun0
    "D0:39:72:BF:CA:A6", # btleArm1
    "D0:39:72:BF:CA:FA", 
    "D0:39:72:BF:CA:81"
]

btleHandshakes = [False] * 3

class ChecksumError(Exception):
    pass

class Comms(DefaultDelegate):
    def __init__(self, serialChar, index):
        DefaultDelegate.__init__(self)
        self.serialChar = serialChar
        self.index = index
        self.buffer = b''
        self.fragmented = 0
        self.dropped = 0
        self.prev = ""

    # def __init__(self, serialChar, index, clientSocket):
    #     DefaultDelegate.__init__(self)
    #     self.serialChar = serialChar
    #     self.index = index
    #     self.clientSocket = clientSocket
    #     self.buffer = b''
    #     self.fragmented = 0
    #     self.dropped = 0
    #     self.prev = ""

    def sendAckPacket(self):
        # print("Sending ack!")
        self.serialChar.write(bytes("A", "utf-8"))

    def handleAckPacket(self):
        self.sendAckPacket()  # TODO: Change to 20bytes
        btleHandshakes[self.index] = True

    def handleDataPacket(self, data, packet):
        # Packet Indexing:
        # 0 - Packet Type
        # 1 - Mean
        # 2 - Range
        # 3 - Variance
        # 4 - Median
        # 5 - Shoots Gun
        # 6 - Gets Shot

        # self.sendAckPacket()
        datas = {
            'BeetleID': self.index,
            'Mean': packet[1],
            'Range': packet[2],
            'Variance': packet[3],
            'Median': packet[4],
            'Has Shot Gun': packet[5],
            'Is Shot': packet[6]
        }
        # print("Beetle {0} data:".format(self.index))
        result = (','.join([str(value) for value in datas.values()]))
        if packet[0] != ord('D'):
            # self.clientSocket.send(data)
            print(result)
        elif result != self.prev:
            print(result)
            self.prev = result
            # self.clientSocket.send(data)
        # print(data)
        self.sendAckPacket()

    def verifyChecksum(self, data):
        # print("start verify")
        packetBytes = struct.unpack('<20b', data)
        # print("unpacked")
        sum = 0
        count = 0
        byte = 0

        for byte in packetBytes:
            if count == 19:  # 19th byte
                if sum == byte:
                    # print("Beetle {0}: Checksum is true, packet valid!".format(self.index))
                    return True
                else:
                    break

            sum ^= byte
            count += 1

        return False

    def handleFragmentation(self, data):
        print("================================")
        print("  ^FRAGMENTED PACKET DETECTED^")
        print("================================")
        self.buffer = self.buffer + data
        self.fragmented += 1
        print("Buffer:", self.buffer)
        print("Data:", data)
        print("Beetle {0} Fragmented: {1}".format(self.index, self.fragmented))
        if len(self.buffer) == 20:  # Need to handle if fragmented weirdly?
            print("================================")
            print("   FRAGMENTED DATA PREVENTED")
            print("================================")
            self.handleNotification(None, self.buffer)
            self.buffer = b''

    def handleChecksumError(self, data):
        print("================================")
        print("Handling checksum error")
        print("================================")
        currBuffer = len(self.buffer)
        # print("received:", data, len(data))
        # print("old data:", self.buffer, currBuffer)
        currData = data[:(20-currBuffer)]
        self.buffer = self.buffer + currData
        print("Fixed data:", self.buffer)
        self.handleNotification(None, self.buffer)
        # print("new called data:")
        # print(self.buffer, len(self.buffer))
        self.buffer = data[(20-currBuffer):]
        print("Leftover data:", self.buffer)
        # print(self.buffer, len(self.buffer))

    def handleNotification(self, charHandle, data):
        try:
            packet = ()
            packetFormat = (
                '<b'  # Packet Type
                'f'   # Mean
                'f'   # Median
                'f'   # Range
                'f'   # Variance
                '?'   # Gun is Shot
                '?'   # Got Shot
                'b'   # Checksum
            )
            # print()
            # print("Beetle {0}: {1} {2}".format(self.index, data, type(data)))
            packet = struct.unpack_from(packetFormat, data, 0)
            if len(packet) == 8:
                if not self.verifyChecksum(data):
                    raise ChecksumError("Incorrect checksum")

            packetType = packet[0]

            if packetType == ord('A'):
                # print("handling ack")
                self.handleAckPacket()
            elif packetType == ord('D') or packetType == ord('G') or packetType == ord('V'):
                # print("handling data")
                self.handleDataPacket(data, packet)

        except struct.error:
            self.handleFragmentation(data)

        except ChecksumError:
            self.handleChecksumError(data)

        except Exception as e:
            self.dropped += 1
            print(e)
            print("Dropped:", data)
            print("Beetle {0} dropped: {1}".format(self.index, self.dropped))

def initHandshake(beetle, serialChar, index):
    # while not btleHandshakes[index]:
    # print("Starting Handshake Protocol...")
    time.sleep(2)
    msg = struct.pack('cffff??b', 'H', 0, 0, 0, 0, False, False, ord("A"))
    # msg = bytes("H", "utf-8")
    serialChar.write(msg)
    # serialChar.write(bytes("H", "utf-8"))

    if beetle.waitForNotifications(TIMEOUT_HANDSHAKE):
        pass


def watchForDisconnect(beetle, index):
    # packetCount = 0
    # interval = 10
    # startTime = time.time()
    while True:
        if not beetle.waitForNotifications(TIMEOUT_NOTIFICATION):
            # disconnected = True
            break
        # packetCount += 1
        # currTime = time.time()
        # if currTime - startTime >= interval:
            # dataRate = (packetCount * 20) / interval
            # print("Beetle {0}: {1} packets over {2}s. Data rate is {3}bytes/s.".format(index, packetCount, interval, dataRate))
            # interval += 10
        # if currTime  - startTime >= TIME_DATA_RATE_COUNT:  
            # return False

    print("No data for 2 seconds, attempting to reconnect...")
    btleHandshakes[index] = False
    beetle.disconnect()  # Disconnects first and try to reconnect again
    return True

def beetleProcess(addr, index):  # Curr beetle addr, curr beetle index
    serialSvc = None
    serialChar = None
    beetle = Peripheral()
    notStop = True

    # with sshtunnel.open_tunnel(
    #     'stu.comp.nus.edu.sg',
    #     ssh_username="danielim",
    #     ssh_password="Cg4002!",
    #     remote_bind_address=('192.168.95.234', BEETLE_PORT),
    # ) as tunnel:

    #     serverName = 'localhost'
    #     serverPort = int(tunnel.local_bind_port)
    #     clientSocket = socket(AF_INET, SOCK_STREAM)
    #     clientSocket.connect((serverName, serverPort))
    #     print("connected to:", serverName, serverPort)

        # dont forget to indent this
    # while notStop:
    try:
        print("Searching for Beetle", str(index))
        beetle.connect(addr)
        print("Connecting to Beetle {0}...".format(index))

        serialSvc = beetle.getServiceByUUID(
            "0000dfb0-0000-1000-8000-00805f9b34fb")
        serialChar = serialSvc.getCharacteristics(
            "0000dfb1-0000-1000-8000-00805f9b34fb")[0]
        delegate = Comms(serialChar, index)
        # delegate = Comms(serialChar, index, clientSocket)
        beetle.withDelegate(delegate)

        time.sleep(3)
        msg = struct.pack("bib", ord("A"), 1, ord("H"))
        print(msg)
        print(len(msg))
        serialChar.write(msg)
        serialChar.write(bytes("S", "utf-8"))
        # serialChar.write(msg)

        beetle.disconnect()

        # if not btleHandshakes[index]:
        #     initHandshake(beetle, serialChar, index)
        #     print("Beetle " + str(index) +": Handshake Successful!")
        #     print("Beetle {0} Handshake Status: {1}".format(index, btleHandshakes[index]))
            


            # if btleHandshakes[index]:
            #     notStop = watchForDisconnect(beetle, index)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    beetle0Process = mp.Process(target=beetleProcess, args=(btleAddrs[3], 0))
    # beetle1Process = mp.Process(target=beetleProcess, args=(btleAddrs[1], 1))
    # beetle2Process = mp.Process(target=beetleProcess, args=(btleAddrs[2], 2))

    try:
        beetle0Process.start()
        # beetle1Process.start()
        # beetle2Process.start()

        beetle0Process.join()
        # beetle1Process.join()
        # beetle2Process.join()
    finally:
        beetle0Process.terminate()
        # beetle1Process.terminate()
        # beetle2Process.terminate()

        print("Closing main")
