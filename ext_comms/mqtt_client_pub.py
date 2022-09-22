import paho.mqtt.client as mqtt

import MQTT

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))



if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(MQTT.Configs.broker, MQTT.Configs.portNum)

    while True:
        toPub = input("are players in same area?")
        ret = client.publish(MQTT.Topics.gameState, toPub)