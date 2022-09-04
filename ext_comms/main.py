import json
from multiprocessing.sharedctypes import SynchronizedBase
import os
import sys
import multiprocessing as mp
import time

import paho.mqtt.client as mqtt

import MQTT
from EvalClient import EvalClient
from GameEngine import GameEngine


def startEngineProcess(evalHost: str, evalPort: int, actionQueue: mp.Queue, isInSameArea: SynchronizedBase):

    evalClient = EvalClient(evalHost, evalPort)
    engine = GameEngine()
    
    gameStateClient = mqtt.Client()
    gameStateClient.connect(MQTT.Configs.broker, MQTT.Configs.portNum)

    try:
        while True:
            inputs = tuple(actionQueue.get(block = True, timeout=100))
            p1_action, p2_action = inputs

            is_in_same_area = True

            with isInSameArea.get_lock():
                is_in_same_area = bool(isInSameArea.value)

            print("engine is carrying out action with bool ", is_in_same_area)

            engine.do_actions(p1_action = p1_action, p2_action=p2_action, is_in_same_area=is_in_same_area)
            print("Now sending to eval server...")
            evalClient.send_data(engine.get_JSON_string())
            resp = evalClient.recv_data()
            respObj = json.loads(resp)
            engine.confirm_player_state(respObj)
            gameStateClient.publish(MQTT.Topics.gameState, resp)

    finally:
        evalClient.close()
        print("successfully closed eval client!")
        gameStateClient.disconnect()
        print("successfully closed MQTT client!")

def startMoveProcess(actionQueue: mp.Queue, inputQueue: mp.Queue):

    while True:
        inputFromQueue = inputQueue.get(block = True)
        todo = str(inputFromQueue).split(' ')
        p1_action = todo[0]
        p2_action = todo[1]
        actionQueue.put((p1_action, p2_action), block=True)


def startAreaClient(isInSameArea):

    def on_connect(client: mqtt.Client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe(MQTT.Topics.inSameArea)

    def on_message(client, userdata, msg):
        nonlocal isInSameArea
        # print(msg.topic + " " + str(msg.payload))
        received = int(msg.payload)
        with isInSameArea.get_lock():
            isInSameArea.value = received
            print(isInSameArea)

    try:
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect(MQTT.Configs.broker, MQTT.Configs.portNum)
        client.loop_forever()

    finally:
        print("disconnecting area client...")
        client.disconnect()


if __name__ == '__main__':
    
    _num_param = 3
    if len(sys.argv) < _num_param:
            print('Invalid number of arguments')
            print('python3 ' + os.path.basename(__file__) + '[Eval Host] [EvalPort]')
            print('Eval Host: IP Address of eval server')
            print('Eval Port: Port number of eval server')
            sys.exit()

    actionQueue = mp.Queue(1)
    inputQueue = mp.Queue(1)
    isInSameArea = mp.Value('i', lock=True)
    isInSameArea.value = 1

    evalHost, evalPort = sys.argv[-2], int(sys.argv[-1])

    engineProcess = mp.Process(target = startEngineProcess, args=(evalHost, evalPort, actionQueue, isInSameArea))
    moveProcess = mp.Process(target = startMoveProcess, args = (actionQueue, inputQueue))
    areaClientProcess = mp.Process(target = startAreaClient, args=(isInSameArea,))

    engineProcess.start()
    moveProcess.start()
    areaClientProcess.start()

    while True:
        time.sleep(1)
        actions = input("Next move: ")
        if actions == "exit":
            inputQueue.close()
            actionQueue.close()
            engineProcess.terminate()
            moveProcess.terminate()
            areaClientProcess.terminate()
            break
        inputQueue.put(actions, block=True)

    engineProcess.join()
    moveProcess.join()
    areaClientProcess.join()

    print("closing main")


