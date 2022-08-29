import json
import os
import sys

from EvalClient import EvalClient
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

    def confirm_player_state(self, correct_resp: dict):
        self.p1.update_correct_state(correct_resp['p1'])
        self.p2.update_correct_state(correct_resp['p2'])

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

    try:

        while True:
            todo = input("Next move: ").split(' ')
            p1_action = todo[0]
            p2_action = todo[1]
            is_in_same_area = todo[2] == "true"

            engine.do_actions(p1_action = p1_action, p2_action=p2_action, is_in_same_area=is_in_same_area)
            print("Now sending to eval server...")
            evalClient.send_data(engine.get_JSON_string())
            resp = evalClient.recv_data()
            respObj = json.loads(resp)
            engine.confirm_player_state(respObj)


    finally:
        evalClient.close()
        print("successfully closed client!")

