import ctypes
import multiprocessing as mp
import struct

from socket import *

NUM_BEETLES = 6
PACKET_LEN = 20
BEETLE_PORT = 6721

P1_VEST = b'V'
P1_GUN = b'G'
P2_VEST = b'W'
P2_GUN = b'J'

P1_ACCEL_X = b'a'
P1_ACCEL_Y = b'b'
P1_ACCEL_Z = b'c'
P1_ROTATE_X = b'd'
P1_ROTATE_Y = b'e'
P1_ROTATE_Z = b'f'

P2_ACCEL_X = b'u'
P2_ACCEL_Y = b'v'
P2_ACCEL_Z = b'w'
P2_ROTATE_X = b'x'
P2_ROTATE_Y = b'y'
P2_ROTATE_Z = b'z'

P1_WRIST = set([P1_ACCEL_X, P1_ACCEL_Y, P1_ACCEL_Z, P1_ROTATE_X, P1_ROTATE_Y, P1_ROTATE_Z])
P2_WRIST = set([P2_ACCEL_X, P2_ACCEL_Y, P2_ACCEL_Z, P2_ROTATE_X, P2_ROTATE_Y, P2_ROTATE_Z])

PACKET_TYPE = 0
MEAN = 1
RANGE = 2
MEDIAN = 3
VARIANCE = 4
DID_SHOOT = 5
IS_SHOT = 6
CHECKSUM = 7

PACKET_FORMAT_STR = "<cffff??b"

def updateWristArr(wristData, packet):

    if packet[PACKET_TYPE] == P1_ACCEL_X or packet[PACKET_TYPE] == P2_ACCEL_X:
        wristData[0:4] = packet[MEAN], packet[RANGE], packet[VARIANCE], packet[MEDIAN]

    elif packet[PACKET_TYPE] == P1_ACCEL_Y or packet[PACKET_TYPE] == P2_ACCEL_Y:
        wristData[4:8] = packet[MEAN], packet[RANGE], packet[VARIANCE], packet[MEDIAN]

    if packet[PACKET_TYPE] == P1_ACCEL_Z or packet[PACKET_TYPE] == P2_ACCEL_Z:
        wristData[8:12] = packet[MEAN], packet[RANGE], packet[VARIANCE], packet[MEDIAN]

    if packet[PACKET_TYPE] == P1_ROTATE_X or packet[PACKET_TYPE] == P2_ROTATE_X:
        wristData[12:16] = packet[MEAN], packet[RANGE], packet[VARIANCE], packet[MEDIAN]

    if packet[PACKET_TYPE] == P1_ROTATE_Y or packet[PACKET_TYPE] == P2_ROTATE_Y:
        wristData[16:20] = packet[MEAN], packet[RANGE], packet[VARIANCE], packet[MEDIAN]

    if packet[PACKET_TYPE] == P1_ROTATE_Z or packet[PACKET_TYPE] == P2_ROTATE_Z:
        wristData[20:] = packet[MEAN], packet[RANGE], packet[VARIANCE], packet[MEDIAN]

class BeetleStruct(ctypes.Structure):
    _fields_ = [('packetType', ctypes.c_char), \
                ('mean', ctypes.c_double), \
                ('range', ctypes.c_double), \
                ('variance', ctypes.c_double), \
                ('median', ctypes.c_double), \
                ('didShoot', ctypes.c_bool), \
                ('isShot', ctypes.c_bool), \
                ('checksum', ctypes.c_byte)]

def startBeetleMainProcess(beetleQueue: mp.Array):
    serverPort = BEETLE_PORT
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("", serverPort))
    serverSocket.listen()
    print('Beetle server is ready to receive message at port', serverPort)

    indivs = [mp.Process() for _ in range(NUM_BEETLES)]

    for i in range(NUM_BEETLES):
        connectionSocket, clientAddr = serverSocket.accept()
        indivs[i] = mp.Process(target = startBeetleIndiv, args = (beetleQueue, i, connectionSocket))
        indivs[i].start()

    for i in range(NUM_BEETLES):
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
