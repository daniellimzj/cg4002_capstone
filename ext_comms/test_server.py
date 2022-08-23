from socket import *
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

if __name__ == "__main__":
    serverPort = 2105
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen()
    print('Server is ready to receive message')
    connectionSocket, clientAddr = serverSocket.accept()

    try:
        message = connectionSocket.recv(48)
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
        connectionSocket.send(bytes(decrypted_message, encoding="utf8"))

    finally:
        connectionSocket.close()
        print("socket closed")
