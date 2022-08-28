# External Communications

## SSH Tunneling

We use an SSH Tunnel from the laptop to Ultra96 like so:

`ssh -L [laptopPort]:192.168.95.234:[ultra96Port] [user]@sunfire.comp.nus.edu.sg` \
e.g. \
`ssh -L 9696:192.168.95.234:9696 danielim@sunfire.comp.nus.edu.sg`