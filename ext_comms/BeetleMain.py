import ctypes
import multiprocessing as mp
import struct

from socket import *

NUM_BEETLES = 6
PACKET_LEN = 17
BEETLE_PORT = 6721

PACKET_FORMAT_STR = "<cffff"

class BeetleStruct(ctypes.Structure):
    _fields_ = [('packetType', ctypes.c_byte), ('mean', ctypes.c_double), ('median', ctypes.c_double), ('range', ctypes.c_double), ('variance', ctypes.c_double)]

def startBeetleMainProcess(beetleArr: mp.Array, beetleQueue: mp.Array):
    serverPort = BEETLE_PORT
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("", serverPort))
    serverSocket.listen()
    print('Server is ready to receive message at port', serverPort)

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
            print(packet)
            while len(packet) < PACKET_LEN:
                packet += connSocket.recv(1)

            print(packet)
            packetType, mean, median, variance, range = struct.unpack(PACKET_FORMAT_STR, packet)

            with beetleArr.get_lock():
                beetleArr[id].packetType = packetType
                beetleArr[id].mean = mean
                beetleArr[id].median = median
                beetleArr[id].variance = variance
                beetleArr[id].range = range
            
                print(beetleArr[id])
            
            beetleQueue.put(id, block=True)


    finally:
        connSocket.close()

