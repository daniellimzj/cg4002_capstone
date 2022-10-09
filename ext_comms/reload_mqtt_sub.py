import multiprocessing as mp
import queue

import paho.mqtt.client as mqtt

import MQTT


# Use id 1 for player 1, and 2 for player 2
def startMQTTClient(id: int, queue: mp.Queue):

    def on_connect(client: mqtt.Client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

        if id == 1:
            client.subscribe(MQTT.Topics.didP1Reload)
        elif id == 2:
            client.subscribe(MQTT.Topics.didP2Reload)

    def on_message(client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))
        queue.put(bool(int(msg.payload)))

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
    
    mqttQueue = mp.Queue()

    mqttClientProcess = mp.Process(target = startMQTTClient, args=(1, mqttQueue))

    mqttClientProcess.start()

    print("mqtt client started, now going to loop")
    
    try:
        while True:
            # Below is just a placeholder
            # for all the random beetle stuff
            pass

            try:
                didPlayerReload = mqttQueue.get()
                print("did player reload", didPlayerReload)
                if didPlayerReload:
                    # Another placeholder
                    # You should send some signal to the beetle here
                    pass

            except queue.Empty:
                continue

    except KeyboardInterrupt:
        mqttClientProcess.terminate()

    finally:
        mqttClientProcess.join()

        

        






