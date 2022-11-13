# Internal Communications

## Installation and Setup (Laptop)

- Install bluepy:
  - $ `sudo apt-get install python3-pip libglib2.0-dev`
  - $ `sudo pip3 install bluepy`
- Update BLE connection interval on Laptop:
  - $ `sudo -i`
  - $ `echo 10 > /sys/kernel/debug/bluetooth/hci0/conn_min_interval`
  - $ `echo 40 > /sys/kernel/debug/bluetooth/hci0/conn_max_interval`

## Installation and Setup (Beetle)

- Configure beetle through AT commands:
  - Open serial monitor
  - Set "Both NL & CR" to "No line ending"
  - Type `+++` and send it
- Enter AT Commands:
  - Set "No line ending" to "Both NL & CR"
  - Mac Address: AT+MAC=?
  - Set UART to 115200: `AT+UART=115200`
  - Set role to peripheral: `AT+UART=ROLE_PERIPHERAL`
  - Set min connection interval: `AT+MIN_INTERVAL=10`
  - Set max connection interval: `AT+MAX_INTERVAL=40`
  - Set debug mode to off: `AT+BLUNO_DEBUG=off`

## Running the Beetles

There are 3 types of beetles each with different hardwares. Each beetle has its own functionalities, therefore have different scripts.

- Beetle Arm:
  - The script is found under int_comms/beetleArmTest2
  - Upload the beetle script
- Beetle Vest:
  - The script is found under int_comms/beetleVest
  - Upload the beetle script
- Beetle Gun:
  - The script is foung under int_comms/beetleGun
  - Upload the beetle script

## Running the Laptop Node:
$ `python3 ble_final_p1.py [PORT_NUMBER]`    
(Make sure that the beetle addresses are correct)
