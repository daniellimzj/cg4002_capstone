import base64
import json
import os
import socket
import sys

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


if __name__ == '__main__':
    _num_param = 2
    if len(sys.argv) < _num_param:
            print('Invalid number of arguments')
            print('python3 ' + os.path.basename(__file__) + '[EvalPort]')
            print('evalPort: Port number of eval server')
            sys.exit()


    serverName = 'localhost'
    serverPort = int(sys.argv[-1])
    print("Connecting to server at %s, port number %s", serverName, serverPort)

    config = json.load(open('config.json'))
    secretKey = bytes(config["key"], encoding="utf8")

    iv = Random.new().read(AES.block_size)
    cipher = AES.new(secretKey, AES.MODE_CBC, iv)

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    msg = bytes(input("Enter a message: "), encoding="utf8")
    msg = pad(msg, AES.block_size)

    print(msg)

    encodedMsg = base64.b64encode(bytes(iv + cipher.encrypt(msg)))

    print(encodedMsg, len(encodedMsg))

    clientSocket.send(encodedMsg)

    received = clientSocket.recv(2048)

    print("from server: ", received.decode())

    clientSocket.close()
