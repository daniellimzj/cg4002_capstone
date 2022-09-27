from socket import *
import struct

packetLen = 17

if __name__ == "__main__":

    serverPort = 9696
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen()
    print('Server is ready to receive message at port', serverPort)
    connectionSocket, clientAddr = serverSocket.accept()

    while True:

        packet = b''
        print(packet)
        while len(packet) < packetLen:
            packet += connectionSocket.recv(1)

        print(packet)
        packetType, mean, median, variance, range = struct.unpack("<cffff", packet)

        print(packetType, mean, median, variance, range)

        