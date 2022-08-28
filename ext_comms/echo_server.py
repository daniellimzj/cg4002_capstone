import os
import sys
from socket import *

if __name__ == "__main__":

    _num_param = 2
    if len(sys.argv) < _num_param:
            print('Invalid number of arguments')
            print('python3 ' + os.path.basename(__file__) + '[port]')
            print('Port: Port to run server on')
            sys.exit()

    serverPort = int(sys.argv[1])
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen()
    print('Server is ready to receive message')
    connectionSocket, clientAddr = serverSocket.accept()
    message = connectionSocket.recv(2048)
    print('Server received: ', str(message))
    connectionSocket.send(message)
    connectionSocket.close()




