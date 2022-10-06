import ctypes
import multiprocessing as mp
import struct

from socket import *

NUM_BEETLES = 6
PACKET_LEN = 20
BEETLE_PORT = 6721

P1_VEST = b'V'
P1_GUN = b'G'
P1_WRIST = b'D'
P2_VEST = b'W'
P2_GUN = b'J'
P2_WRIST = b'E'

PACKET_TYPE_TO_INDEX = {b'V': 0, b'G': 1, b'D': 2, b'W': 3, b'J': 4, b'E': 5}

PACKET_TYPE = 0
MEAN = 1
RANGE = 2
MEDIAN = 3
VARIANCE = 4
DID_SHOOT = 5
IS_SHOT = 6
CHECKSUM = 7

PACKET_FORMAT_STR = "<cffff??b"

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
            print(packet[PACKET_TYPE], packet[MEAN], packet[RANGE], packet[VARIANCE], packet[MEDIAN], packet[DID_SHOOT], packet[IS_SHOT], packet[CHECKSUM])
            
            beetleQueue.put(packet, block=True)

    finally:
        connSocket.close()

