import json
import multiprocessing as mp
import os
import sys
import time
from multiprocessing.sharedctypes import SynchronizedBase
from socket import *

import paho.mqtt.client as mqtt

import BeetleMain as beetles
import MQTT
from EvalClient import EvalClient
from GameEngine import GameEngine
from Player import Actions


def startEngineProcess(evalHost: str, evalPort: int, actionQueue: mp.Queue, isInSameArea: SynchronizedBase):

    evalClient = EvalClient(evalHost, evalPort)
    engine = GameEngine()
    
    gameStateClient = mqtt.Client()
    gameStateClient.connect(MQTT.Configs.broker, MQTT.Configs.portNum)

    try:
        while True:
            inputs = tuple(actionQueue.get(block = True, timeout=1000))
            p1_action, p2_action, is_p1_shot, is_p2_shot = inputs

            can_p1_see_p2 = True
            can_p2_see_p1 = True

            if p1_action == Actions.shoot:
                can_p1_see_p2 = is_p2_shot

            if p2_action == Actions.shoot:
                can_p2_see_p1 = is_p1_shot
            
            if p1_action != Actions.shoot and p2_action != Actions.shoot:
                with isInSameArea.get_lock():
                    can_p1_see_p2 = bool(isInSameArea.value)
                    can_p2_see_p1 = bool(isInSameArea.value)

            print("engine is carrying out action with bools", can_p1_see_p2, can_p2_see_p1)
            engine.do_actions(p1_action, p2_action, can_p1_see_p2, can_p2_see_p1)

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

def startMoveProcess(actionQueue: mp.Queue, beetleQueue: mp.Queue):

    received = {}

    p1Move = Actions.no
    p2Move = Actions.no
    didP1GetShot = False
    didP2GetShot = False

    while True:
        try:
            (beetleID, packet) = beetleQueue.get(block = True, timeout = 0.5)
            received[beetleID] = packet

            if beetleID == beetles.P1_WRIST:
                p1Move  = getMoveFromAI(beetleID)

            elif beetleID == beetles.P2_WRIST:
                p2Move = getMoveFromAI(beetleID)

            elif beetleID == beetles.P1_GUN:
                p1Move = Actions.shoot

            elif beetleID == beetles.P2_GUN:
                p2Move = Actions.shoot

            elif beetleID == beetles.P1_VEST:
                didP1GetShot = True
            
            elif beetleID == beetles.P2_VEST:
                didP2GetShot = True       

        except:
            continue

        finally:
            if p1Move != Actions.no or p2Move != Actions.no:
                actionQueue.put((p1Move, p2Move, didP1GetShot, didP2GetShot), block=True)
                p1Move = Actions.no
                p2Move = Actions.no
                didP1GetShot = False
                didP2GetShot = False

def getMoveFromAI(id):
    pass

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

    beetleQueue = mp.Queue(beetles.NUM_BEETLES * 3)

    evalHost, evalPort = sys.argv[-2], int(sys.argv[-1])

    engineProcess = mp.Process(target = startEngineProcess, args=(evalHost, evalPort, actionQueue, isInSameArea))
    moveProcess = mp.Process(target = startMoveProcess, args = (actionQueue, beetleQueue))
    areaClientProcess = mp.Process(target = startAreaClient, args=(isInSameArea,))
    beetleMainProcess = mp.Process(target = beetles.startBeetleMainProcess, args=(beetleQueue,))

    try:
        engineProcess.start()
        moveProcess.start()
        areaClientProcess.start()   
        beetleMainProcess.start()
        

        engineProcess.join()
        moveProcess.join()
        areaClientProcess.join()
        beetleMainProcess.join()

    finally:
        actionQueue.close()
        engineProcess.terminate()
        moveProcess.terminate()
        areaClientProcess.terminate()
        beetleMainProcess.terminate()
        print("closing main")


