import json
import multiprocessing as mp
import os
import sys
from multiprocessing.sharedctypes import SynchronizedBase

import paho.mqtt.client as mqtt

import MQTT
from EvalClient import EvalClient
from Player import Actions, Player

def startAreaClient(isInSameArea: SynchronizedBase):

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


def startEngineProcess(evalHost: str, evalPort: int, actionQueue: mp.Queue, isInSameArea: SynchronizedBase):

    runWithEval = evalHost and evalPort
    evalClient = None

    if runWithEval:
        evalClient = EvalClient(evalHost, evalPort)
    engine = GameEngine()
    
    gameStateClient = mqtt.Client()
    gameStateClient.connect(MQTT.Configs.broker, MQTT.Configs.portNum)

    try:
        while True:
            inputs = tuple(actionQueue.get(block = True))
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

            if runWithEval:
                print("Now sending to eval server...")
                evalClient.send_data(currState)
                resp = evalClient.recv_data()
                respObj = json.loads(resp)
                engine.check_and_update_player_states(respObj)
                gameStateClient.publish(MQTT.Topics.gameState, resp)

            else:
                gameStateClient.publish(MQTT.Topics.gameState, currState)

    finally:
        if runWithEval:
            evalClient.close()
            print("successfully closed eval client!")
        
        gameStateClient.disconnect()
        print("successfully closed MQTT client!")


class GameEngine:

    def __init__(self):
        self.gameState = {}

        self.p1 = Player(1)
        self.p2 = Player(2)

    def get_JSON_string(self):
        return json.dumps({'p1': self.p1.get_dict(), 'p2': self.p2.get_dict()})

    def do_actions(self, p1_action = Actions.no, p2_action = Actions.no, can_p1_see_p2 = False, can_p2_see_p1=False):
        is_p1_action_valid = self.p1.is_action_valid(p1_action)
        is_p2_action_valid = self.p2.is_action_valid(p2_action)

        self.p1.update(can_p2_see_p1, p1_action, p2_action, is_p2_action_valid)
        self.p2.update(can_p1_see_p2, p2_action, p1_action, is_p1_action_valid)

    def check_and_update_player_states(self, correct_resp: dict) -> bool:
        is_p1_state_correct = self.p1.check_and_update_correct_state(correct_resp['p1'])
        is_p2_state_correct = self.p2.check_and_update_correct_state(correct_resp['p2'])

        return is_p1_state_correct and is_p2_state_correct

if __name__ == '__main__':

    _num_param = 3
    if len(sys.argv) < _num_param:
            print('Invalid number of arguments')
            print('python3 ' + os.path.basename(__file__) + '[Eval Host] [EvalPort]')
            print('Eval Host: IP Address of eval server')
            print('Eval Port: Port number of eval server')
            sys.exit()

    evalClient = None

    runWithEval = False

    if runWithEval:
        evalClient = EvalClient(sys.argv[-2], int(sys.argv[-1]))
    engine = GameEngine()
    
    mqttClient = mqtt.Client()
    mqttClient.connect(MQTT.Configs.broker, MQTT.Configs.portNum)

    try:

        while True:
            todo = input("Next move: ").split(' ')
            p1_action = todo[0]
            p2_action = todo[1]
            can_p1_see_p2 = todo[2] == "true"
            can_p2_see_p1 = todo[3] == "true"

            engine.do_actions(p1_action, p2_action, can_p1_see_p2, can_p2_see_p1)

            currState = engine.get_JSON_string()

            if runWithEval:
                print("Now sending to eval server...")
                evalClient.send_data(currState)
                resp = evalClient.recv_data()
                respObj = json.loads(resp)
                engine.check_and_update_player_states(respObj)
                mqttClient.publish(MQTT.Topics.gameState, resp)

            else:
                mqttClient.publish(MQTT.Topics.gameState, currState)


    finally:
        if runWithEval:
            evalClient.close()
            print("successfully closed eval client!")
        mqttClient.disconnect()
        print("successfully closed MQTT client!")

