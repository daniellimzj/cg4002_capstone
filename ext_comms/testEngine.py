import json
import os
import sys

import paho.mqtt.client as mqtt

import MQTT
from Player import Actions, Player


class GameEngine:

    def __init__(self):
        self.gameState = {}

        self.p1 = Player(1)
        self.p2 = Player(2)

    def get_JSON_string(self):
        return json.dumps({'p1': self.p1.get_dict(), 'p2': self.p2.get_dict()})

    def do_actions(self, p1_action = Actions.no, p2_action = Actions.no, is_in_same_area = False):
        is_p1_action_valid = self.p1.is_action_valid(p1_action)
        is_p2_action_valid = self.p2.is_action_valid(p2_action)

        self.p1.update(is_in_same_area, p1_action, p2_action, is_p2_action_valid)
        self.p2.update(is_in_same_area, p2_action, p1_action, is_p1_action_valid)

    def check_and_update_player_states(self, correct_resp: dict) -> bool:
        is_p1_state_correct = self.p1.check_and_update_correct_state(correct_resp['p1'])
        is_p2_state_correct = self.p2.check_and_update_correct_state(correct_resp['p2'])

        return is_p1_state_correct and is_p2_state_correct

if __name__ == '__main__':

    engine = GameEngine()
    
    mqttClient = mqtt.Client()
    mqttClient.connect(MQTT.Configs.broker, MQTT.Configs.portNum)

    try:

        while True:
            todo = input("Next move: ").split(' ')
            p1_action = todo[0]
            p2_action = todo[1]
            is_in_same_area = True

            engine.do_actions(p1_action = p1_action, p2_action=p2_action, is_in_same_area=is_in_same_area)
            currState = engine.get_JSON_string()

            mqttClient.publish(MQTT.Topics.gameState, currState)

    finally:
        print("successfully closed eval client!")
        mqttClient.disconnect()
        print("successfully closed MQTT client!")
