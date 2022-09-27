import asyncio
import platform
import sys
import struct

from bleak import BleakClient, BleakScanner
from bleak.exc import BleakError

beetleIDs = [
    "D0:39:72:BF:CA:CF",
    "17AE54AA-415D-4B76-AD40-F90E21A7F343"
]

beetleHandshakes = [False] * 3


# class BLEComms():
#     def __init__(self, beetle, serialCharacteristic, index):
#         self.beetle = beetle
#         self.serialCharacteristic = serialCharacteristic
#         self.index = index
#
#    def ackHandler(self):
#        self.beetle.write_gatt_char(self.serialCharacteristic, bytes("A", "utf-8"))
#        beetleHandshakes[self.index] = True
#
#     def notificationHandler(self, sender, data):
#         # TODO: Verify the checksum
#         try:
#             packetFormat = {
#                 '<b' # Packet Type (1)
#                 '7h' # Data (14)
#                 'l' # Timestamp (4)
#                 'b' # Checksum (1)
#             }

#             packet = struct.unpack(packetFormat, data)
#             packetType = packet[0]

#             if packetType == ord('A'):
#                 self.ackHandler()

#         except Exception as e:
#             raise BleakError(e)

# def initHandshake(beetle, serialCharacteristic, index):
#     while not beetleHandshakes[index]:
#         print("Sending hello to Beetle", str(index))
#         beetle.write_gatt_char(serialCharacteristic, bytes("H", "utf-8"))


# async def beetleThread(idList, index):
#     isFirstLoop = True
#     serialService = None
#     serialCharacteristic = None

#     while True:
#         try:
#             print("Searching for Beetle", str(index))
#             device = await BleakScanner.find_device_by_address(idList, timeout=5.0)

#             print("Connecting to Beetle...", str(index))
#             async with BleakClient(device) as beetle:
#                 print("Beetle connected: {beetle.is_connected}")
#                 if isFirstLoop:
#                     serialService = beetle.services.get_service("0000dfb0-0000-1000-8000-00805f9b34fb")
#                     serialCharacteristic = serialService.get_characteristic("0000dfb1-0000-1000-8000-00805f9b34fb")
#                     # print(serialCharacteristic)
#                     comms = BLEComms(beetle, serialCharacteristic, index)
#                     beetle.start_notify(serialCharacteristic, comms.notificationHandler)


#                 print("Initialising handshake for Beetle", str(index))
#                 initHandshake(beetle, serialCharacteristic, index)


#         except Exception as e:
#             raise BleakError(f"A device with address {idList} could not be found.")

def notificationHandler(sender, data):
    print("{0}: {1}".format(sender, data))


async def beetleThread(idList, index):
    isFirstLoop = True
    serialService = None
    serialCharacteristic = None

    # while True:
    try:
        print("Searching for Beetle", str(index))
        device = await BleakScanner.find_device_by_address(idList[index], timeout=10.0)

        print("Connecting to Beetle", str(index))
        async with BleakClient(device) as beetle:
            print("Beetle connected: {beetle.is_connected}")
            if isFirstLoop:
                serialService = beetle.services.get_service("0000dfb0-0000-1000-8000-00805f9b34fb")
                serialCharacteristic = serialService.get_characteristic("0000dfb1-0000-1000-8000-00805f9b34fb")
                print(serialCharacteristic)
                await beetle.start_notify("0000dfb1-0000-1000-8000-00805f9b34fb", notificationHandler)
                # await beetle.write_gatt_char(serialCharacteristic, bytes("A", "utf-8"))
                await asyncio.sleep(5.0)
                await beetle.stop_notify("0000dfb1-0000-1000-8000-00805f9b34fb")
                # comms = BLEComms(beetle, serialCharacteristic, index)
                # beetle.start_notify(serialCharacteristic, comms.notificationHandler)

            # print("Initialising handshake for Beetle", str(index))
            # initHandshake(beetle, serialCharacteristic, index)


    except Exception as e:
        print(e)


# async def main(ble_address: str):
#     device = await BleakScanner.find_device_by_address(ble_address, timeout=5.0)
# if not device:
#     raise BleakError(f"A device with address {ble_address} could not be found.")
#     async with BleakClient(device) as client:
#         svcs = await client.get_services()
#         print("Services:")
#         for service in svcs:
#             print(service)


if __name__ == "__main__":
    # asyncio.run(beetleThread(sys.argv[1] if len(sys.argv) == 2 else beetleIDs[0]))
    # asyncio.run(main(sys.argv[1] if len(sys.argv) == 2 else beetleIDs[0]))
    asyncio.run(beetleThread(beetleIDs, 0))