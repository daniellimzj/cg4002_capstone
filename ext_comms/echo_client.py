import os
import sys
from socket import *

if __name__ == "__main__":

    _num_param = 3
    if len(sys.argv) < _num_param:
            print('Invalid number of arguments')
            print('python3 ' + os.path.basename(__file__) + '[host] [port]')
            print('Host: Host to connect to')
            print('Port: Port to connect to')
            sys.exit()

    serverName = sys.argv[1]
    serverPort = sys.argv[2]
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    print("connected to:", serverName, serverPort)
    message = input('Enter a message: ')
    clientSocket.send(message.encode())
    receivedMsg = clientSocket.recv(2048)
    print("Received back:", receivedMsg)