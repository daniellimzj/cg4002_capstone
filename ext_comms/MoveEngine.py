from Player import Actions

import multiprocessing as mp
import BeetleMain as beetles
from cg4002_capstone.hw_ai.real_data.predictor.main import MoveClassifier

def startMoveProcess(actionQueue: mp.Queue, beetleQueue: mp.Queue):

    classifier = MoveClassifier()

    while True:
        p1Move, p2Move, didP1GetShot, didP2GetShot = getMoves(beetleQueue, classifier)

        if p1Move != Actions.no or p2Move != Actions.no:
            actionQueue.put((p1Move, p2Move, didP1GetShot, didP2GetShot), block=True)

def getMoves(beetleQueue: mp.Queue, classifier: MoveClassifier):
    p1Move = Actions.no
    p2Move = Actions.no

    p1WristData = [0.0 * 24]
    p2WristData = [0.0 * 24]

    didP1GetShot = False
    didP2GetShot = False

    p1WristUpdated = set()
    p2WristUpdated = set()

    packet = beetleQueue.get(block = True)
    beetleID = packet[beetles.PACKET_TYPE]

    if beetleID in beetles.P1_WRIST:
        beetles.updateWristArr(p1WristData, packet)
        p1WristUpdated.add(beetleID)

    elif beetleID in beetles.P2_WRIST:
        beetles.updateWristArr(p2WristData, packet)
        p2WristUpdated.add(beetleID)

    elif beetleID == beetles.P1_GUN:
        p1Move = Actions.shoot

    elif beetleID == beetles.P2_GUN:
        p2Move = Actions.shoot

    elif beetleID == beetles.P1_VEST:
        didP1GetShot = True
            
    elif beetleID == beetles.P2_VEST:
        didP2GetShot = True 

    for _ in range(20):
        try:
            packet = beetleQueue.get(block = True, timeout=0.025)
            beetleID = packet[beetles.PACKET_TYPE]

            if beetleID in beetles.P1_WRIST:
                beetles.updateWristArr(p1WristData, packet)
                p1WristUpdated.add(beetleID)

            elif beetleID in beetles.P2_WRIST:
                beetles.updateWristArr(p2WristData, packet)
                p2WristUpdated.add(beetleID)

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

    if p1Move != Actions.shoot and p1WristUpdated == beetles.P1_WRIST:
        p1Move = classifier.classifyMove(p1WristData)

    if p2Move != Actions.shoot and p2WristUpdated == beetles.P2_WRIST:
        p2Move = classifier.classifyMove(p2WristData)

    return p1Move, p2Move, didP1GetShot, didP2GetShot


def getMoveFromAI(packet):
    pass