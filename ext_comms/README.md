# External Communications

## SSH Tunneling

We use an SSH Tunnel from the laptop to Ultra96 like so:

`ssh -L [laptopPort]:192.168.95.234:[ultra96Port] [user]@sunfire.comp.nus.edu.sg` \
e.g. \
`ssh -L 9696:192.168.95.234:9696 danielim@sunfire.comp.nus.edu.sg`

Or we can also do the following: \

In these cases, the "destination" is "localhost" because it is the localhost of the server we are using to SSH.

On the laptop: \
`ssh -L 9696:localhost:9696 danielim@sunfire.comp.nus.edu.sg` \
On Sunfire: \
`ssh -L 9696:localhost:9696 xilinx@192.168.95.234`

## Running the HiveMQ CE Broker:
```
cd hivemq-ce-2022.1/
bin/run.sh
```

## Running the Game Engine:
`python3 GameEngine.py [eval server host] [eval server port]`