import json
import multiprocessing as mp
import os
import sys
import time
from multiprocessing.sharedctypes import SynchronizedBase

import paho.mqtt.client as mqtt

import MQTT
from EvalClient import EvalClient
from Player import Actions, Player


def startPlayerClient(canPlayerSeeOther: SynchronizedBase, id: int):

    def on_connect(client: mqtt.Client, userdata, flags, rc):
        print("Player client connected with result code "+str(rc))

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
        print("running with eval server")
        evalClient = EvalClient(evalHost, evalPort)
    engine = GameEngine()
    
    try:

        gameStateClient = mqtt.Client()
        gameStateRes = None
        while gameStateRes != mqtt.MQTT_ERR_SUCCESS:
            print("game state client connecting...")
            gameStateRes = gameStateClient.connect(MQTT.Configs.broker, MQTT.Configs.portNum)
        print("game state client connected!")
        gameStateClient.loop_start()

        reloadClient = mqtt.Client()
        reloadRes = None
        while reloadRes != mqtt.MQTT_ERR_SUCCESS:
            print("reload client connecting...")
            reloadRes = reloadClient.connect(MQTT.Configs.broker, MQTT.Configs.portNum)
        print("reload client connected!")
        reloadClient.loop_start()

        numWrong = 0
        numDone = 0
    
        while True:
            inputs = tuple(actionQueue.get(block = True))

            p1_action, p2_action, is_p1_shot, is_p2_shot = inputs

            can_p1_see_p2 = True
            can_p2_see_p1 = True

            old_p1_grenades, old_p2_grenades = engine.get_grenade_counts()
            old_p1_bullets, old_p2_bullets = engine.get_bullet_counts()
            old_p1_num_shields, old_p2_num_shields = engine.get_shield_counts()
            old_p1_shield_time, old_p2_shield_time = engine.get_shield_times()

            if p1_action == Actions.shoot:
                can_p1_see_p2 = is_p2_shot
            elif p1_action == Actions.grenade:
                with canP1SeeP2.get_lock():
                    can_p1_see_p2 = bool(canP1SeeP2.value)

            if p2_action == Actions.shoot:
                can_p2_see_p1 = is_p1_shot
            elif p2_action == Actions.grenade:
                with canP2SeeP1.get_lock():
                    can_p2_see_p1 = bool(canP2SeeP1.value)
            
            print("game engine doing", p1_action, p2_action, can_p1_see_p2, can_p2_see_p1)
            engine.do_actions(p1_action, p2_action, can_p1_see_p2, can_p2_see_p1)

            currState = engine.get_JSON_string()

            if runWithEval:
                # print("Now sending to eval server...")
                evalClient.send_data(currState)
                resp = evalClient.recv_data()
                respObj = json.loads(resp)
                engine.check_and_update_player_states(respObj)

            new_p1_action, new_p2_action = engine.get_player_actions()
            if p1_action != new_p1_action:
                numWrong += 1
            if p2_action != new_p2_action:
                numWrong += 1
            numDone += 2

            print("so far got", numWrong, "wrong out of", numDone)

            p1_action, p2_action = engine.get_player_actions()

            if p1_action == Actions.grenade and old_p1_grenades == 0:
                print("setting p1 grenade action to invalid")
                engine.p1.set_action(Actions.grenadeInvalid)

            elif p1_action == Actions.reload and old_p1_bullets > 0:
                print("setting p1 reload action to invalid")
                engine.p1.set_action(Actions.reloadInvalid)

            elif p1_action == Actions.shield and (old_p1_num_shields == 0 or old_p1_shield_time > 0):
                print("setting p1 shield action to invalid")
                engine.p1.set_action(Actions.shieldInvalid)


            if p2_action == Actions.grenade and old_p2_grenades == 0:
                print("setting p2 grenade action to invalid")
                engine.p2.set_action(Actions.grenadeInvalid)

            elif p2_action == Actions.reload and old_p2_bullets > 0:
                print("setting p2 reload action to invalid")
                engine.p2.set_action(Actions.reloadInvalid)

            elif p2_action == Actions.shield and (old_p2_num_shields == 0 or old_p2_shield_time > 0):
                print("setting p2 shield action to invalid")
                engine.p2.set_action(Actions.shieldInvalid)

            currState = engine.get_JSON_string()
            
            gameStateClient.publish(MQTT.Topics.gameState, currState)

            new_p1_bullets, new_p2_bullets = engine.get_bullet_counts()

            if p1_action == Actions.reload and old_p1_bullets == 0 and new_p1_bullets == 6:
                print("sending p1 reload to gun")
                reloadClient.publish(MQTT.Topics.didP1Reload, "1")

            if p2_action == Actions.reload and old_p2_bullets == 0 and new_p2_bullets == 6:
                print("sending p2 reload to gun")
                reloadClient.publish(MQTT.Topics.didP2Reload, "1")

    finally:
        if runWithEval:
            evalClient.close()
            print("successfully closed eval client!")
        
        gameStateClient.loop_stop()
        gameStateClient.disconnect()
        reloadClient.loop_stop()
        reloadClient.disconnect()
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

    def get_shield_counts(self):
        return self.p1.get_shield_count(), self.p2.get_shield_count()

    def get_shield_times(self):
        return self.p1.get_shield_time(), self.p2.get_shield_time()

    def get_grenade_counts(self):
        return self.p1.get_grenade_count(), self.p2.get_grenade_count()

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

    runWithEval = True

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

