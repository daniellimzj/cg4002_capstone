from asyncio import current_task
import json
import os
import sys

import paho.mqtt.client as mqtt

import MQTT
from EvalClient import EvalClient
from Player import Actions, Player


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

            mqttClient.publish(MQTT.Topics.gameState, currState)
            evalClient.send_data(currState)

            resp = evalClient.recv_data()
            respObj = json.loads(resp)

            if not engine.check_and_update_player_states(respObj):
                print("Since state was not correct, publishing correct state to MQTT")
                mqttClient.publish(MQTT.Topics.gameState, resp)


    finally:
        evalClient.close()
        print("successfully closed eval client!")
        mqttClient.disconnect()
        print("successfully closed MQTT client!")

