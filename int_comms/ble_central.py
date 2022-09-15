import struct
import multiprocessing as mp
import time

from bluepy.btle import Peripheral, DefaultDelegate

TIMEOUT_NOTIFICATION = 2 #s
TIMEOUT_HANDSHAKE = 50/100 #s

TIME_DATA_RATE_COUNT = 70 #s

btleAddrs = [
    "D0:39:72:BF:CA:CF",
    "D0:39:72:BF:CA:FA",
    "D0:39:72:BF:CA:81"
]

btleHandshakes = [False] * 3

# AckPacket = struct.pack('<bffff??b', ord("A"), float(0), float(0), float(0), float(0), False, False, ord("A"))


class Comms(DefaultDelegate):
    def __init__(self, serialChar, index):
        DefaultDelegate.__init__(self)
        self.serialChar = serialChar
        self.index = index
        self.buffer = b''

    def sendAckPacket(self):
        # print("Sending ack!")
        self.serialChar.write(bytes("A", "utf-8"))

    def handleAckPacket(self):
        self.sendAckPacket()  # TODO: Change to 20bytes
        btleHandshakes[self.index] = True

    def handleDataPacket(self, packet):
        # Packet Indexing:
        # 0 - Packet Type
        # 1 - Mean
        # 2 - Median
        # 3 - Standard Deviation
        # 4 - Range
        # 5 - Shoots Gun
        # 6 - Gets Shot

        # self.sendAckPacket()
        data = {
            'BeetleID': self.index,
            'Mean': packet[1],
            'Median': packet[2],
            'Standard Deviation': packet[3],
            'Range': packet[4],
            'Has Shot Gun': packet[5],
            'Is Shot': packet[6]
        }
        print("Beetle {0} data:".format(self.index))
        print((','.join([str(value) for value in data.values()])))
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
                    print("Beetle {0}: Checksum is true, packet valid!".format(self.index))
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
        if len(self.buffer) == 20:  # Need to handle if fragmented weirdly?
            print("================================")
            print("   FRAGMENTED DATA PREVENTED")
            print("================================")
            self.handleNotification(None, self.buffer)
            self.buffer = b''

    def handleNotification(self, charHandle, data):
        try:
            # print("handling notification now")
            packet = ()
            packetFormat = (
                '<b'  # Packet Type
                'f'   # Mean
                'f'   # Median
                'f'   # Standard Deviation
                'f'   # Range
                '?'   # Gun is Shot
                '?'   # Got Shot
                'b'   # Checksum
            )
            print()
            print("Beetle {0}: {1} {2}".format(self.index, data, type(data)))
            packet = struct.unpack_from(packetFormat, data, 0)
            # print(packet)
            # for i in packet:
            #     print(i, type(i))
            # print(len(packet))
            if len(packet) == 8:
                # print("hi")
                if not self.verifyChecksum(data):
                    raise Exception("Incorrect checksum")
                # packet = struct.unpack(packetFormat, data)

            packetType = packet[0]

            if packetType == ord('A'):
                # print("handling ack")
                self.handleAckPacket()
            elif packetType == ord('D'):
                # print("handling data")
                self.handleDataPacket(packet)

        except struct.error:
            self.handleFragmentation(data)
            # # print("********************************")
            # # print("STRUCT ERROR")
            # self.buffer = self.buffer + data
            # if len(self.buffer) == 20:  # Need to handle if fragmented weirdly?
            #     # print("FRAGMENTED DATA PREVENTED")
            #     print(self.buffer)
            #     self.handleNotification(None, self.buffer)
            #     self.buffer = b''

        except Exception as e:
            print(e, type(e))


def initHandshake(beetle, serialChar, index):
    while not btleHandshakes[index]:
        # print("Starting Handshake Protocol...")
        serialChar.write(bytes("H", "utf-8"))

        if beetle.waitForNotifications(TIMEOUT_HANDSHAKE):
            pass


def watchForDisconnect(beetle, index):
    packetCount = 0
    startTime = time.time()
    while True:
        if not beetle.waitForNotifications(TIMEOUT_NOTIFICATION):
            # runs here if disconnected
            # disconnected = True
            break
        packetCount += 1
        if time.time() - startTime >= TIME_DATA_RATE_COUNT:
            dataRate = (packetCount * 20) / TIME_DATA_RATE_COUNT
            print("Beetle {0}: {1} packets over {2}s. Data rate is {3}bytes/s.".format(index, packetCount, TIME_DATA_RATE_COUNT, dataRate))
            return False

    print("No data for 2 seconds, attempting to reconnect...")
    btleHandshakes[index] = False
    beetle.disconnect()  # Disconnects first and try to reconnect again
    return True

def beetleProcess(addr, index):  # Curr beetle addr, curr beetle index
    serialSvc = None
    serialChar = None
    beetle = Peripheral()
    notStop = True

    while notStop:
        try:
            print("Searching for Beetle", str(index))
            beetle.connect(addr)
            print("Connecting to Beetle {0}...".format(index))

            serialSvc = beetle.getServiceByUUID(
                "0000dfb0-0000-1000-8000-00805f9b34fb")
            serialChar = serialSvc.getCharacteristics(
                "0000dfb1-0000-1000-8000-00805f9b34fb")[0]
            delegate = Comms(serialChar, index)
            beetle.withDelegate(delegate)

            if not btleHandshakes[index]:
                initHandshake(beetle, serialChar, index)
                print("Beetle " + str(index) +": Handshake Successful!")
                print("Beetle {0} Handshake Status: {1}".format(index, btleHandshakes[index]))

            if btleHandshakes[index]:
                notStop = watchForDisconnect(beetle, index)

        except KeyboardInterrupt:
            beetle.disconnect()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    beetle0Process = mp.Process(target=beetleProcess, args=(btleAddrs[0], 0))
    beetle1Process = mp.Process(target=beetleProcess, args=(btleAddrs[1], 1))
    beetle2Process = mp.Process(target=beetleProcess, args=(btleAddrs[2], 2))

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
