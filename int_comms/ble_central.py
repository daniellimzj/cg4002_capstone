import struct
import multiprocessing as mp

from bluepy.btle import Peripheral, DefaultDelegate

# TODO: Implement Workaround for weird fragmentation: 11bytes + 20bytes + 9bytes
# TODO: Standardise packets to 20 bytes

TIMEOUT_NOTIFICATION = 5
TIMEOUT_HANDSHAKE = 50/100

btleAddrs = [
    "D0:39:72:BF:CA:CF",
    "D0:39:72:BF:CA:FA",
    "D0:39:72:BF:CA:CF"
]

btleHandshakes = [False] * 3


class Comms(DefaultDelegate):
    def __init__(self, serialChar, index):
        DefaultDelegate.__init__(self)
        self.serialChar = serialChar
        self.index = index
        self.buffer = b''

    def sendAckPacket(self):
        print("Sending ack!")
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
        print((','.join([str(value) for value in data.values()])))
        # print(data)
        self.sendAckPacket()

    def verifyChecksum(self, data):
        print("start verify")
        packetBytes = struct.unpack('<20b', data)
        print("unpacked")
        sum = 0
        count = 0
        byte = 0

        for byte in packetBytes:
            if count == 19:  # 19th byte
                if sum == byte:
                    print("Checksum is true, packet valid!")
                    return True
                else:
                    break

            sum ^= byte
            count += 1

        return False

    def handleNotification(self, charHandle, data):
        try:
            print("handling notification now")
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
            print(data, type(data))
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
                print("handling ack")
                self.handleAckPacket()
            elif packetType == ord('D'):
                print("handling data")
                self.handleDataPacket(packet)

        except struct.error:
            print("********************************")
            print("STRUCT ERROR")
            self.buffer = self.buffer + data
            if len(self.buffer) == 20:  # Need to handle if fragmented weirdly?
                print("FRAGMENTED DATA PREVENTED")
                print(self.buffer)
                self.handleNotification(None, self.buffer)
                self.buffer = b''

        except Exception as e:
            print(e, type(e))


def initHandshake(beetle, serialChar, index):
    while not btleHandshakes[index]:
        print("Starting Handshake Protocol...")
        serialChar.write(bytes("H", "utf-8"))

        if beetle.waitForNotifications(TIMEOUT_HANDSHAKE):
            pass


def watchForDisconnect(beetle, index):
    while True:
        if not beetle.waitForNotifications(TIMEOUT_NOTIFICATION):
            break

    print("No data for 5 seconds, attempting to reconnect...")
    btleHandshakes[index] = False
    beetle.disconnect()  # Disconnects first and try to reconnect again


def beetleThread(addr, index):  # Curr beetle addr, curr beetle index
    serialSvc = None
    serialChar = None
    beetle = Peripheral()

    while True:
        try:
            print("Searching for Beetle", str(index))
            beetle.connect(addr)
            print("Connecting...")

            serialSvc = beetle.getServiceByUUID(
                "0000dfb0-0000-1000-8000-00805f9b34fb")
            serialChar = serialSvc.getCharacteristics(
                "0000dfb1-0000-1000-8000-00805f9b34fb")[0]
            delegate = Comms(serialChar, index)
            beetle.withDelegate(delegate)

            if not btleHandshakes[index]:
                initHandshake(beetle, serialChar, index)
                print("Handshake Successful!")
                print(btleHandshakes)
                isFirstLoop = False

            if btleHandshakes[index]:
                watchForDisconnect(beetle, index)

        except KeyboardInterrupt:
            beetle.disconnect()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    beetle0Process = mp.Process(target=beetleThread, args=(btleAddrs[0], 0))
    # beetle1Process = mp.Process(target=beetleThread, args=(btleAddrs[1], 1))
    # beetle2Process = mp.Process(target=beetleThread, args=(btleAddrs[2], 2))

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
