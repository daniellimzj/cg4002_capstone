import json
import sshtunnel
from socket import *

if __name__ == "__main__":

    config = json.load(open('config.json'))
    sunfirePassword = config["sunfirePassword"]

    with sshtunnel.open_tunnel(
        'stu.comp.nus.edu.sg',
        ssh_username="danielim",
        ssh_password=sunfirePassword,
        remote_bind_address=('192.168.95.234', 9696),
        local_bind_address=('localhost', 9696)
    ) as tunnel:
            serverName = 'localhost'
            serverPort = int(tunnel.local_bind_port)
            clientSocket = socket(AF_INET, SOCK_STREAM)
            clientSocket.connect((serverName, serverPort))
            print("connected to:", serverName, serverPort)
            message = input('Enter a message: ')
            clientSocket.send(message.encode())
            receivedMsg = clientSocket.recv(2048)
            print("Received back:", receivedMsg)
    