import json
from multiprocessing.sharedctypes import SynchronizedBase
import os
from socket import *
import sys
import multiprocessing as mp

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

            print("engine is carrying out action with bool", is_in_same_area)
            engine.do_actions(p1_action = p1_action, p2_action=p2_action, is_in_same_area=is_in_same_area)

            currState = engine.get_JSON_string()
            print("Now sending to eval server...")
            evalClient.send_data(currState)
            gameStateClient.publish(MQTT.Topics.gameState, currState)

            resp = evalClient.recv_data()
            respObj = json.loads(resp)
            if not engine.check_and_update_player_states(respObj):
                gameStateClient.publish(MQTT.Topics.gameState, resp)

    finally:
        evalClient.close()
        print("successfully closed eval client!")
        gameStateClient.disconnect()
        print("successfully closed MQTT client!")

def startMoveProcess(actionQueue: mp.Queue):

    serverPort = 9696
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen()
    print('Server is ready to receive message at port', serverPort)
    connectionSocket, clientAddr = serverSocket.accept()

    while True:
        message = connectionSocket.recv(2048)
        todo = message.decode().split(' ')
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

    actionQueue = mp.Queue()
    isInSameArea = mp.Value('i', lock=True)
    isInSameArea.value = 1

    evalHost, evalPort = sys.argv[-2], int(sys.argv[-1])

    engineProcess = mp.Process(target = startEngineProcess, args=(evalHost, evalPort, actionQueue, isInSameArea))
    moveProcess = mp.Process(target = startMoveProcess, args = (actionQueue,))
    areaClientProcess = mp.Process(target = startAreaClient, args=(isInSameArea,))

    try:
        engineProcess.start()
        moveProcess.start()
        areaClientProcess.start()

        engineProcess.join()
        moveProcess.join()
        areaClientProcess.join()

    finally:
        actionQueue.close()
        engineProcess.terminate()
        moveProcess.terminate()
        areaClientProcess.terminate()
        print("closing main")


