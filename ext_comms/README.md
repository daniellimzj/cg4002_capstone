# External Communications


## Installation and Setup
- Follow the instructions in `/eval_server` to install dependencies and set up the evaluation server
- The only other dependencies used are:
    - sshtunnel: https://pypi.org/project/sshtunnel/
    - paramiko: https://www.paramiko.org/

## SSH Tunneling

We use a manual setup for the SSH tunnelling like so:

On the laptop: \
`ssh -L 9696:localhost:9696 danielim@stu.comp.nus.edu.sg` \
On the stu.comp.nus.edu.sg server: \
`ssh -L 9696:localhost:9696 xilinx@192.168.95.234`

In these cases, the "destination" is "localhost" because it is the localhost of the server we are using to SSH.

### Legacy Methods

Before Sunfire was deprecated and replaced by stu.comp.nus.edu.sg, there were two methods that worked as well. For completeness sake and in case the new server ever supports these methods, we will keep them below:

There are two Python files `ssh_test.py` and `ssh_tunnel.py` that automatically sets up the SSH tunnel for usage in our code. 

Alternatively, we can manually use an SSH Tunnel from the laptop to Ultra96 like so:

`ssh -L [laptopPort]:192.168.95.234:[ultra96Port] [user]@stu.comp.nus.edu.sg` \
e.g. \
`ssh -L 9696:192.168.95.234:9696 danielim@stu.comp.nus.edu.sg`


## Running the HiveMQ CE Broker Locally:
To run a local instance of the MQTT broker, can refer to the following documentation:
https://github.com/hivemq/hivemq-community-edition

Once downloaded, the broker can be run like so:
```
cd hivemq-ce-2022.1/
bin/run.sh
```

## Running the Game Engine:
`python3 GameEngine.py [eval server host] [eval server port]`

## Other files:
There are a variety of other files in this subdirectory that make it easy to test standalone parts. For example, `mqtt_client_sub.py` allows one to easily test MQTT functionality, and `echo_server.py` can test if a simple TCP/IP connection is working.