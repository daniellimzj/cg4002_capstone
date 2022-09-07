import paho.mqtt.client as mqtt

import MQTT

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT.Topics.gameState)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

if __name__ == "__main__":
    try:
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message

        client.connect(MQTT.Configs.broker, MQTT.Configs.portNum, 60)

        while True:
            client.publish(MQTT.Topics.gameState, input("are players in same area?"))


    finally:
        client.disconnect()