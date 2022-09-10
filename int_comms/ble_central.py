from bluepy.btle import Peripheral, DefaultDelegate
import struct

# TODO: Implement Handshake
# TODO: Test handshake functionality
# TODO: Standardise packets to 20 bytes
# TODO: Handle packet fragmentation; wait for 20 bytes of data before processing

TIMEOUT_HANDSHAKE = 50

btleAddrs = [
    "D0:39:72:BF:CA:CF",
    "D0:39:72:BF:CA:CF",
    "D0:39:72:BF:CA:CF"
]

btleHandshakes = [False] * 3


class Comms(DefaultDelegate):
    def __init__(self, serialChar, index):
        DefaultDelegate.__init__(self)
        self.serialChar = serialChar
        self.index = index

    def sendAckPacket(self):
        self.serialChar.write(bytes("A", "utf-8"))

    def handleAckPacket(self):
        self.sendAckPacket()  # TODO: Change to 20bytes
        btleHandshakes[self.index] = True

    def verifyChecksum(self, data):
        packetBytes = struct.unpack('<20b', data)
        sum = 0
        count = 0
        byte = 0

        for byte in packetBytes:
            if count == 19:  # 19th byte
                if sum == byte:
                    return True
                else:
                    break

            sum ^= byte
            count += 1

        return False

    def handleNotification(self, charHandle, data):
        try:
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
            if struct.calcsize(data) == 20:
                if not self.verifyChecksum(data):
                    raise Exception("Incorrect checksum")
                packet = struct.unpack(packetFormat, data)

            packetType = packet[0]

            if packetType == ord('A'):
                self.handleAckPacket()
            elif packetType == ord('D'):
                self.handleDataPacket(packet)

        except Exception as e:
            print(e)


def initHandshake(beetle, serialChar, index):
    while not btleHandshakes[index]:
        print("Sending Hello Packet")
        serialChar.write(bytes("H", "utf-8"))

        if beetle.waitForNotifications(TIMEOUT_HANDSHAKE):
            pass


def beetleThread(addr, index):  # Curr beetle addr, curr beetle index
    isFirstLoop = True
    serialSvc = None
    serialChar = None
    beetle = Peripheral()

    try:
        print("Searching for Beetle", str(index))
        beetle.connect(addr)
        print("Connecting...")

        if isFirstLoop:
            serialSvc = beetle.getServiceByUUID(
                "0000dfb0-0000-1000-8000-00805f9b34fb")
            serialChar = serialSvc.getCharacteristics(
                "0000dfb1-0000-1000-8000-00805f9b34fb")
            delegate = Comms(serialChar, index)
            beetle.withDelegate(delegate)

        if not btleHandshakes[index]:
            initHandshake(beetle, serialChar, index)

    except Exception as e:
        print(e)
