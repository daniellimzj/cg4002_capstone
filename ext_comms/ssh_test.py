import json
import sshtunnel
from socket import *

if __name__ == "__main__":

    config = json.load(open('config.json'))
    password = bytes(config["sshPassword"], encoding="utf-8")


    with sshtunnel.open_tunnel(
        'sunfire.comp.nus.edu.sg',
        ssh_username="danielim",
        ssh_password=password,
        local_bind_address=('localhost', 9696),
        remote_bind_address=('192.168.95.234', 9696)
    ) as tunnel:

        serverName = 'localhost'
        serverPort = 9696
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        message = input('Enter a message: ')
        clientSocket.send(message.encode())
        receivedMsg = clientSocket.recv(2048)

