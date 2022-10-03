import os
import sys
from socket import *
import struct

from BeetleMain import BEETLE_PORT

if __name__ == "__main__":


    serverName = "localhost"
    serverPort = BEETLE_PORT
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    print("connected to:", serverName, serverPort)

    while True:
        temp = input()
        packet = struct.pack("<cffff", b'd', 0.0, 0.1, 0.2, 0.3)
        clientSocket.send(packet)
