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

def startBeetleMainProcess(beetleArr: mp.Array, beetleQueue: mp.Array):
    serverPort = BEETLE_PORT
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("", serverPort))
    serverSocket.listen()
    print('Beetle server is ready to receive message at port', serverPort)

    indivs = [mp.Process() for _ in range(NUM_BEETLES)]

    for i in range(NUM_BEETLES):
        connectionSocket, clientAddr = serverSocket.accept()
        indivs[i] = mp.Process(target = startBeetleIndiv, args = (beetleArr, beetleQueue, i, connectionSocket))
        indivs[i].start()

    for i in range(NUM_BEETLES):
        indivs[i].join()

def startBeetleIndiv(beetleArr: mp.Array, beetleQueue: mp.Queue, id: int, connSocket: socket):
    try:
        while True:
            packet = b''
            while len(packet) < PACKET_LEN:
                packet += connSocket.recv(1)

            packetType, mean, range, variance, median, didShoot, isShot, checksum = struct.unpack(PACKET_FORMAT_STR, packet)

            with beetleArr.get_lock():
                beetleArr[id].packetType = packetType
                beetleArr[id].mean = mean
                beetleArr[id].range = range
                beetleArr[id].variance = variance
                beetleArr[id].median = median
                beetleArr[id].didShoot = didShoot
                beetleArr[id].isShot = isShot
                beetleArr[id].checksum = checksum
                
            
                print(id, beetleArr[id].packetType, beetleArr[id].mean, beetleArr[id].range, beetleArr[id].variance, beetleArr[id].median, beetleArr[id].didShoot, beetleArr[id].isShot, beetleArr[id].checksum)
            
            beetleQueue.put(id, block=True)


    finally:
        connSocket.close()

