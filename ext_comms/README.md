# External Communications

## Installation and Setup
- Follow the instructions in `/eval_server` to install dependencies and set up the evaluation server
- The only other dependencies used are:
    - sshtunnel: https://pypi.org/project/sshtunnel/
    - paramiko: https://www.paramiko.org/
    - paho MQTT https://pypi.org/project/paho-mqtt/

## SSH Tunneling

The file `ssh_tunnel.py` shows an example of how to set up the SSH tunnelling in Python.

Alternatively, there are two ways to manually set up the SSH tunnel:

### In 2 commands:
`ssh -L 9696:localhost:9696 danielim@stu.comp.nus.edu.sg` \
On the stu.comp.nus.edu.sg server: \
`ssh -L 9696:localhost:9696 xilinx@192.168.95.234`

The same actions can be done by replacing `stu.comp.nus.edu.sg` with `sunfire.comp.nus.edu.sg`

### In 1 command:

`ssh -L [laptopPort]:192.168.95.234:[ultra96Port] [user]@stu.comp.nus.edu.sg` \
e.g. \
`ssh -L 9696:192.168.95.234:9696 danielim@stu.comp.nus.edu.sg`


## Running the Game Engine:
`python3 main.py [eval server host] [eval server port]` \
If there is a need to run the game engine without the evaluation server, it can be done with:
`python3 main.py`

## Running the Eval Server:
On the Ultra96, perform the following: \
`cd eval_server` \
`export DISPLAY=:0` \
`python3 eval_server.py [port] [group] [players]`
