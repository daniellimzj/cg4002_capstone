import paho.mqtt.client as mqtt

import MQTT


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))



if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(MQTT.Configs.broker, MQTT.Configs.portNum)

    while True:
        playerNum = input("Player that successfully reloaded: ")

        if playerNum == "1":
            client.publish(MQTT.Topics.didP1Reload, "1")

        else:
            client.publish(MQTT.Topics.didP2Reload, "1")
