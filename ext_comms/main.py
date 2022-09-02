import json
import os
import sys
from multiprocessing import Process, Queue
import time

import paho.mqtt.client as mqtt

import MQTT
from EvalClient import EvalClient
from GameEngine import GameEngine


def startEngineProcess(evalHost: str, evalPort: int, actionQueue: Queue):

    evalClient = EvalClient(evalHost, evalPort)
    engine = GameEngine()
    
    mqttClient = mqtt.Client()
    mqttClient.connect(MQTT.Configs.broker, MQTT.Configs.portNum)

    try:
        while True:
            inputs = tuple(actionQueue.get(block = True, timeout=100))
            p1_action, p2_action, is_in_same_area = inputs
            engine.do_actions(p1_action = p1_action, p2_action=p2_action, is_in_same_area=is_in_same_area)
            print("Now sending to eval server...")
            evalClient.send_data(engine.get_JSON_string())
            resp = evalClient.recv_data()
            respObj = json.loads(resp)
            engine.confirm_player_state(respObj)
            mqttClient.publish(MQTT.Topics.gameState, resp)

    finally:
        evalClient.close()
        print("successfully closed eval client!")
        mqttClient.disconnect()
        print("successfully closed MQTT client!")

def startMoveProcess(actionQueue: Queue, inputQueue: Queue):

    while True:
        inputFromQueue = inputQueue.get(block = True)
        todo = str(inputFromQueue).split(' ')
        p1_action = todo[0]
        p2_action = todo[1]
        is_in_same_area = todo[2] == "true"
        actionQueue.put((p1_action, p2_action, is_in_same_area), block=True)

if __name__ == '__main__':
    
    _num_param = 3
    if len(sys.argv) < _num_param:
            print('Invalid number of arguments')
            print('python3 ' + os.path.basename(__file__) + '[Eval Host] [EvalPort]')
            print('Eval Host: IP Address of eval server')
            print('Eval Port: Port number of eval server')
            sys.exit()

    actionQueue = Queue(1)
    inputQueue = Queue(1)
    evalHost, evalPort = sys.argv[-2], int(sys.argv[-1])

    engineProcess = Process(target = startEngineProcess, args=(evalHost, evalPort, actionQueue))
    moveProcess = Process(target = startMoveProcess, args = (actionQueue, inputQueue))

    engineProcess.start()
    moveProcess.start()

    while True:
        time.sleep(1)
        actions = input("Next move: ")
        if actions == "exit":
            inputQueue.close()
            actionQueue.close()
            engineProcess.terminate()
            moveProcess.terminate()
            break
        inputQueue.put(actions, block=True)

    engineProcess.join()
    moveProcess.join()

    print("closing main")


