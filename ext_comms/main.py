import multiprocessing as mp
import os
import sys
from socket import *

import BeetleMain as beetles
from GameEngine import startEngineProcess, startPlayerClient
from MoveEngine import startMoveProcess

if __name__ == '__main__':
    
    _num_param = 3

    actionQueue = mp.Queue()

    canP1SeeP2 = mp.Value('i', lock=True)
    canP2SeeP1 = mp.Value('i', lock=True)
    canP1SeeP2.value = 1
    canP2SeeP1.value = 1

    beetleQueue = mp.Queue(beetles.NUM_BEETLES * 3)

    evalHost, evalPort = "", 0

    if len(sys.argv) == _num_param:
        evalHost, evalPort = sys.argv[-2], int(sys.argv[-1])

    beetlePort = int(input("Please input the port for beetle: "))

    engineProcess = mp.Process(target = startEngineProcess, args=(evalHost, evalPort, actionQueue, canP1SeeP2, canP2SeeP1))
    moveProcess = mp.Process(target = startMoveProcess, args = (actionQueue, beetleQueue))

    p1ClientProcess = mp.Process(target = startPlayerClient, args=(canP1SeeP2, 1))
    p2ClientProcess = mp.Process(target = startPlayerClient, args=(canP2SeeP1, 2))

    beetleMainProcess = mp.Process(target = beetles.startBeetleMainProcess, args=(beetleQueue, beetlePort))

    try:
        engineProcess.start()
        moveProcess.start()
        p1ClientProcess.start()
        p2ClientProcess.start()      
        beetleMainProcess.start()
        

        engineProcess.join()
        moveProcess.join()
        p1ClientProcess.join()
        p2ClientProcess.join()
        beetleMainProcess.join()

    finally:
        actionQueue.close()
        beetleQueue.close()
        engineProcess.terminate()
        moveProcess.terminate()
        p1ClientProcess.terminate()
        p2ClientProcess.terminate()
        beetleMainProcess.terminate()
        print("closing main")
