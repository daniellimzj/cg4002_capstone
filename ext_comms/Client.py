import base64
import json
import socket

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


class Client:

    def __init__(self, serverName: str, serverPort: int):

        print("Connecting to server at ", serverName, ", port number ", serverPort)

        config = json.load(open('config.json'))
        secretKey = bytes(config["key"], encoding="utf-8")

        self.iv = Random.new().read(AES.block_size)
        self.cipher = AES.new(secretKey, AES.MODE_CBC, self.iv)

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((serverName, serverPort))

    def send_data(self, data: str):

        print("trying to send: ", data)
        msg = bytes(data, encoding="utf-8")
        msg = pad(msg, AES.block_size)

        encodedMsg = base64.b64encode(bytes(self.iv + self.cipher.encrypt(msg)))

        messageLen = bytes(str(len(encodedMsg)), encoding="utf-8")

        print(messageLen + b"_" + encodedMsg)

        self.socket.sendall(messageLen + b"_" + encodedMsg)

    def recv_data(self) -> str:
        try:
            # recv length followed by '_' followed by cypher
            data = b''
            while not data.endswith(b'_'):
                _d = self.socket.recv(1)
                if not _d:
                    data = b''
                    break
                data += _d
            if len(data) == 0:
                print('while waiting for length, no more data from the client')

            data = data.decode("utf-8")
            length = int(data[:-1])

            data = b''
            while len(data) < length:
                _d = self.socket.recv(length - len(data))
                if not _d:
                    data = b''
                    break
                data += _d
            if len(data) == 0:
                print('while getting message, no more data from the client')
                
            msg = data.decode("utf-8")  # Decode raw bytes to UTF-8
            return msg

        except ConnectionResetError:
            print('Connection Reset')

    def close(self):
        self.socket.close()
