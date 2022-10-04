import ctypes
import multiprocessing as mp
import struct

from socket import *

NUM_BEETLES = 6
PACKET_LEN = 20
BEETLE_PORT = 6721

P1_VEST = 0
P1_GUN = 1
P1_WRIST = 2
P2_VEST = 3
P2_GUN = 4
P2_WRIST = 5

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
    try:
        while True:
            packet = b''
            while len(packet) < PACKET_LEN:
                packet += connSocket.recv(1)

            packet = struct.unpack(PACKET_FORMAT_STR, packet)
            print(id, packet[PACKET_TYPE], packet[MEAN], packet[RANGE], packet[VARIANCE], packet[MEDIAN], packet[DID_SHOOT], packet[IS_SHOT], packet[CHECKSUM])
            
            beetleQueue.put((id, *packet), block=True)

    finally:
        connSocket.close()

