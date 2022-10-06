import multiprocessing as mp
import MQTT
import paho.mqtt.client as mqtt

def startPlayerClient(id: int):

    def on_connect(client: mqtt.Client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        if id == 1:
            client.subscribe(MQTT.Topics.canP1SeeP2)
        elif id == 2:
            client.subscribe(MQTT.Topics.canP2SeeP1)

    def on_message(client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))

    try:
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect(MQTT.Configs.broker, MQTT.Configs.portNum)
        client.loop_forever()

    finally:
        print("disconnecting player", id, "client...")
        client.disconnect()



if __name__ == "__main__":

    p1ClientProcess = mp.Process(target = startPlayerClient, args=(1,))
    p2ClientProcess = mp.Process(target = startPlayerClient, args=(2,))

    try:
        p1ClientProcess.start()
        p2ClientProcess.start()

        p1ClientProcess.join()
        p2ClientProcess.join()

    except KeyboardInterrupt:
        p1ClientProcess.terminate()
        p2ClientProcess.terminate()