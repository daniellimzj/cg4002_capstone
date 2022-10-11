import json
import multiprocessing as mp
import os
import sys
from multiprocessing.sharedctypes import SynchronizedBase

import paho.mqtt.client as mqtt

import MQTT
from EvalClient import EvalClient
from Player import Actions, Player


def startPlayerClient(canPlayerSeeOther: SynchronizedBase, id: int):

    def on_connect(client: mqtt.Client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        if id == 1:
            client.subscribe(MQTT.Topics.canP1SeeP2)
        elif id == 2:
            client.subscribe(MQTT.Topics.canP2SeeP1)

    def on_message(client, userdata, msg):
        nonlocal canPlayerSeeOther
        # print(msg.topic + " " + str(msg.payload))
        received = int(msg.payload)
        with canPlayerSeeOther.get_lock():
            canPlayerSeeOther.value = received

    try:
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect(MQTT.Configs.broker, MQTT.Configs.portNum)
        client.loop_forever()

    finally:
        print("disconnecting player", id, "client...")
        client.disconnect()


def startEngineProcess(evalHost: str, evalPort: int, actionQueue: mp.Queue, canP1SeeP2: SynchronizedBase, canP2SeeP1: SynchronizedBase):

    runWithEval = evalHost and evalPort
    evalClient = None

    if runWithEval:
        evalClient = EvalClient(evalHost, evalPort)
    engine = GameEngine()
    
    mqttClient = mqtt.Client()
    mqttClient.connect(MQTT.Configs.broker, MQTT.Configs.portNum)

    try:
        while True:
            inputs = tuple(actionQueue.get(block = True))

            p1_action, p2_action, is_p1_shot, is_p2_shot = inputs

            can_p1_see_p2 = True
            can_p2_see_p1 = True

            prev_p1_bullets, prev_p2_bullets = engine.get_bullet_counts()

            if p1_action == Actions.shoot:
                can_p1_see_p2 = is_p2_shot
            else:
                with canP1SeeP2.get_lock():
                    can_p1_see_p2 = bool(canP1SeeP2.value)

            if p2_action == Actions.shoot:
                can_p2_see_p1 = is_p1_shot
            else:
                with canP2SeeP1.get_lock():
                    can_p2_see_p1 = bool(canP2SeeP1.value)
            

            print("received from move engine:", inputs)
            print("engine is carrying out action with bools", can_p1_see_p2, can_p2_see_p1)
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

            p1_action, p2_action = engine.get_player_actions()
            new_p1_bullets, new_p2_bullets = engine.get_bullet_counts()

            if prev_p1_bullets == 0 and p1_action == Actions.reload and new_p1_bullets == 6:
                print("sending p1 reload")
                mqttClient.publish(MQTT.Topics.didP1Reload, "1")

            if prev_p2_bullets == 0 and p2_action ==Actions.reload and new_p2_bullets == 6:
                print("sending p2 reload")
                mqttClient.publish(MQTT.Topics.didP2Reload, "1")

    finally:
        if runWithEval:
            evalClient.close()
            print("successfully closed eval client!")
        
        mqttClient.disconnect()
        print("successfully closed MQTT client!")


class GameEngine:

    def __init__(self):
        self.gameState = {}

        self.p1 = Player(1)
        self.p2 = Player(2)

    def get_JSON_string(self):
        return json.dumps({'p1': self.p1.get_dict(), 'p2': self.p2.get_dict()})

    def get_bullet_counts(self):
        return self.p1.get_bullet_count(), self.p2.get_bullet_count()

    def get_player_actions(self):
        return self.p1.get_action(), self.p2.get_action()

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

