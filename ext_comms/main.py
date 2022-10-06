import multiprocessing as mp
import os
import sys
from socket import *

import BeetleMain as beetles
from GameEngine import startAreaClient, startEngineProcess
from MoveEngine import startMoveProcess

if __name__ == '__main__':
    
    _num_param = 3

    if len(sys.argv) < _num_param or (len(sys.argv) != 2 and sys.argv[1] != "-n"):
            print('To run with eval server:')
            print('python3 ' + os.path.basename(__file__) + '[Eval Host] [EvalPort]')
            print('Eval Host: IP Address of eval server')
            print('Eval Port: Port number of eval server')
            print("")
            print("To run without eval server:")
            print('python3 ' + os.path.basename(__file__) + '-n')
            sys.exit()

    actionQueue = mp.Queue()

    isInSameArea = mp.Value('i', lock=True)
    isInSameArea.value = 1

    beetleQueue = mp.Queue(beetles.NUM_BEETLES * 3)

    evalHost, evalport = None, None

    if len(sys.argv) == _num_param:
        evalHost, evalPort = sys.argv[-2], int(sys.argv[-1])

    engineProcess = mp.Process(target = startEngineProcess, args=(evalHost, evalPort, actionQueue, isInSameArea))
    moveProcess = mp.Process(target = startMoveProcess, args = (actionQueue, beetleQueue))
    areaClientProcess = mp.Process(target = startAreaClient, args=(isInSameArea,))
    beetleMainProcess = mp.Process(target = beetles.startBeetleMainProcess, args=(beetleQueue,))

    try:
        engineProcess.start()
        moveProcess.start()
        areaClientProcess.start()   
        beetleMainProcess.start()
        

        engineProcess.join()
        moveProcess.join()
        areaClientProcess.join()
        beetleMainProcess.join()

    finally:
        actionQueue.close()
        engineProcess.terminate()
        moveProcess.terminate()
        areaClientProcess.terminate()
        beetleMainProcess.terminate()
        print("closing main")


