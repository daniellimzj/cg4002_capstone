import os
import sys
from socket import *

if __name__ == "__main__":

    serverName = 'localhost'
    serverPort = 9696
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    print("connected to:", serverName, serverPort)

    try:
        while True:
            message = input("Enter players' actions: ")
            clientSocket.send(message.encode())

    finally:
        clientSocket.close()