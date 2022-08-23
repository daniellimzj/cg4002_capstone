from socket import *
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_message(message):

    print(message)
    decoded_message = base64.b64decode(message)                            # Decode message from base64 to bytes
    print(decoded_message)
    iv              = decoded_message[:AES.block_size]                                     # Get IV value
    print(iv)
    secret_key      = bytes("abcdabcdabcdabcd", encoding="utf8")             # Convert secret key to bytes
    print(secret_key)

    cipher = AES.new(secret_key, AES.MODE_CBC, iv)                              # Create new AES cipher object

    decrypted_message = cipher.decrypt(decoded_message[AES.block_size:])  # Perform decryption
    print(decrypted_message)
    decrypted_message = unpad(decrypted_message, AES.block_size)
    print(decrypted_message)
    decrypted_message = decrypted_message.decode('utf8')  # Decode bytes into utf-8
    print(decrypted_message)

    return decrypted_message

if __name__ == "__main__":
    serverPort = 2106
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen()
    print('Server is ready to receive message')
    connectionSocket, clientAddr = serverSocket.accept()

    try:
        # recv length followed by '_' followed by cypher
        data = b''
        while not data.endswith(b'_'):
            print(data)
            _d = connectionSocket.recv(1)
            if not _d:
                data = b''
                break
            data += _d
        if len(data) == 0:
            print('no more data from the client')

        data = data.decode("utf-8")
        length = int(data[:-1])

        data = b''
        while len(data) < length:
            _d = connectionSocket.recv(length - len(data))
            if not _d:
                data = b''
                break
            data += _d
        if len(data) == 0:
            print('no more data from the client')
            
        msg = data.decode("utf8")  # Decode raw bytes to UTF-8
        print(msg)
        finalMsg = decrypt_message(msg)
        connectionSocket.send(bytes(finalMsg, encoding="utf8"))


    except ConnectionResetError:
        print('Connection Reset')

    finally:
        connectionSocket.close()
        print("socket closed")



