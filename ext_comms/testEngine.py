import json
import os
import sys

import paho.mqtt.client as mqtt

import MQTT
from Player import Actions, Player
from GameEngine import GameEngine

if __name__ == '__main__':

    engine = GameEngine()
    
    gameStateClient = mqtt.Client()
    gameStateClient.connect(MQTT.Configs.broker, MQTT.Configs.portNum)

    try:

        while True:
            todo = input("Next move: ").split(' ')
            p1_action = todo[0]
            p2_action = todo[1]
            is_in_same_area = True

            old_p1_grenades, old_p2_grenades = engine.get_grenade_counts()
            old_p1_bullets, old_p2_bullets = engine.get_bullet_counts()
            old_p1_num_shields, old_p2_num_shields = engine.get_shield_counts()
            old_p1_shield_time, old_p2_shield_time = engine.get_shield_times()

            
            engine.do_actions(p1_action, p2_action, True, True)

            currState = engine.get_JSON_string()

            p1_action, p2_action = engine.get_player_actions()

            if p1_action == Actions.grenade and old_p1_grenades == 0:
                print("setting p1 grenade action to invalid")
                engine.p1.set_action(Actions.grenadeInvalid)
                currState = engine.get_JSON_string()

            elif p1_action == Actions.reload and old_p1_bullets > 0:
                print("setting p1 reload action to invalid")
                engine.p1.set_action(Actions.reloadInvalid)
                currState = engine.get_JSON_string()

            elif p1_action == Actions.shield and (old_p1_num_shields == 0 or old_p1_shield_time > 0):
                print("setting p1 shield action to invalid")
                engine.p1.set_action(Actions.shieldInvalid)
                currState = engine.get_JSON_string()


            if p2_action == Actions.grenade and old_p2_grenades == 0:
                print("setting p2 grenade action to invalid")
                engine.p2.set_action(Actions.grenadeInvalid)
                currState = engine.get_JSON_string()

            elif p2_action == Actions.reload and old_p2_bullets > 0:
                print("setting p2 reload action to invalid")
                engine.p2.set_action(Actions.reloadInvalid)
                currState = engine.get_JSON_string()

            elif p2_action == Actions.shield and (old_p2_num_shields == 0 or old_p2_shield_time > 0):
                print("setting p2 shield action to invalid")
                engine.p2.set_action(Actions.shieldInvalid)
                currState = engine.get_JSON_string()
            

            print(currState)
            gameStateClient.publish(MQTT.Topics.gameState, currState, qos=2)


    finally:
        print("successfully closed eval client!")
        gameStateClient.disconnect()
        print("successfully closed MQTT client!")

