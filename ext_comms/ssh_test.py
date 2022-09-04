import json
import sshtunnel
from socket import *

if __name__ == "__main__":

    config = json.load(open('config.json'))
    sunfirePassword = config["sunfirePassword"]
    xilinxPassword = config["xilinxPassword"]

    with sshtunnel.open_tunnel(
        ssh_address_or_host=('sunfire.comp.nus.edu.sg', 22),
        ssh_username="danielim",
        ssh_password=sunfirePassword,
        remote_bind_address=('192.168.95.234', 22),
        local_bind_address=('localhost', 6969)
    ) as tunnel1:
        print('Connection to Sunfire from port ' + str(tunnel1.local_bind_port) + " OK...")
        with sshtunnel.open_tunnel(
            ssh_address_or_host=('localhost', tunnel1.local_bind_port),
            remote_bind_address=('127.0.0.1', 9696),
            local_bind_address=('127.0.0.1', 9696),
            ssh_username='xilinx',
            ssh_password=xilinxPassword,
        ) as tunnel2:

            serverName = 'localhost'
            serverPort = 9696
            clientSocket = socket(AF_INET, SOCK_STREAM)
            clientSocket.connect((serverName, serverPort))
            print("connected to:", serverName, serverPort)
            message = input('Enter a message: ')
            clientSocket.send(message.encode())
            receivedMsg = clientSocket.recv(2048)
            print("Received back:", receivedMsg)