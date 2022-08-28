# External Communications

## SSH Tunneling

We use a double SSH Tunnel:

From Sunfire to Ultra96:

`ssh -L [sunfirePortNum]:192.168.95.234:[ultra96PortNum] [user]@192.168.95.234` \
e.g. \
`ssh -L 9696:192.168.95.234:9696 xilinx@192.168.95.234`


From laptop to Sunfire:

`ssh -L [laptopPortNum]:sunfire.comp.nus.edu.sg:[sunfirePortNum] [user]@sunfire.comp.nus.edu.sg` \
e.g. \
`ssh -L 9696:sunfire.comp.nus.edu.sg:9696 danielim@sunfire.comp.nus.edu.sg`