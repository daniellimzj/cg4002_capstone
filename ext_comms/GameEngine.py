import json

from Player import Actions, Player


class GameEngine:

    def __init__(self):
        self.gameState = {}

        self.p1 = Player()
        self.p2 = Player()

    def get_JSON_string(self):
        return json.dumps({'p1': self.p1.get_dict(), 'p2': self.p2.get_dict()})

    def do_actions(self, p1_action = Actions.no, p2_action = Actions.no, is_in_same_area = False):
        is_p1_action_valid = self.p1.is_action_valid(p1_action)
        is_p2_action_valid = self.p2.is_action_valid(p2_action)

        self.p1.update(is_in_same_area, p1_action, p2_action, is_p2_action_valid)
        self.p2.update(is_in_same_area, p2_action, p1_action, is_p1_action_valid)


if __name__ == '__main__':

    engine = GameEngine()

    while True:
        todo = input().split(' ')
        p1_action = todo[0]
        is_in_same_area = todo[1] == "true"

        engine.do_actions(p1_action = p1_action, is_in_same_area=is_in_same_area)

        print(engine.get_JSON_string())

