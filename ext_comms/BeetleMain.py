import ctypes
import multiprocessing as mp
import struct

from socket import *

NUM_BEETLES = 6
PACKET_LEN = 20
BEETLE_PORT = 6721

# Vests are currently swapped for 1 player game
P1_VEST = b'W'
P1_GUN = b'G'
P1_WRIST = b'D'
P2_VEST = b'V'
P2_GUN = b'J'
P2_WRIST = b'E'

PACKET_TYPE = 0
ACCEL_X = 1
ACCEL_Y = 2
ACCEL_Z = 3
ROTATE_X = 4
ROTATE_Y = 5
ROTATE_Z = 6
DID_SHOOT = 11
IS_SHOT = 12
CHECKSUM = 13

PACKET_FORMAT_STR = "<chhhhhhbbbb??b"

class BeetleStruct(ctypes.Structure):
    _fields_ = [('packetType', ctypes.c_char), \
                ('accelX', ctypes.c_int16), \
                ('accelY', ctypes.c_int16), \
                ('accelZ', ctypes.c_int16), \
                ('rotateX', ctypes.c_int16), \
                ('rotateY', ctypes.c_int16), \
                ('rotateZ', ctypes.c_int16), \
                ('pad1', ctypes.c_bool), \
                ('pad2', ctypes.c_bool), \
                ('pad3', ctypes.c_bool), \
                ('pad4', ctypes.c_bool), \
                ('didShoot', ctypes.c_bool), \
                ('isShot', ctypes.c_bool), \
                ('checksum', ctypes.c_byte)]

def startBeetleMainProcess(beetleQueue: mp.Array):
    serverPort = BEETLE_PORT
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("", serverPort))
    serverSocket.listen()
    print('Beetle server is ready to receive message at port', serverPort)

    indivs = [mp.Process() for _ in range(NUM_BEETLES * 5)]

    for i in range(NUM_BEETLES * 5):
        connectionSocket, clientAddr = serverSocket.accept()
        indivs[i] = mp.Process(target = startBeetleIndiv, args = (beetleQueue, i, connectionSocket))
        indivs[i].start()

    for i in range(NUM_BEETLES * 5):
        indivs[i].join()

def startBeetleIndiv(beetleQueue: mp.Queue, id: int, connSocket: socket):

    print("starting beetle process", id)
    try:
        while True:
            packet = b''
            while len(packet) < PACKET_LEN:
                packet += connSocket.recv(1)

            packet = struct.unpack(PACKET_FORMAT_STR, packet)
            # print(packet[PACKET_TYPE], packet[MEAN], packet[RANGE], packet[VARIANCE], packet[MEDIAN], packet[DID_SHOOT], packet[IS_SHOT], packet[CHECKSUM])
            
            beetleQueue.put(packet, block=True)

    finally:
        connSocket.close()

