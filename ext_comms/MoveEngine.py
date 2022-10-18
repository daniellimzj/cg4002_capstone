import multiprocessing as mp
import statistics
import time as time

import numpy as np
import pandas as pd
from pynq import Overlay, allocate

import BeetleMain as beetles
from Player import Actions

INDEX_TO_ACTION_MAP = {1: "grenade", 2: "reload", 3: "shield", 4: "logout", 5: "none"}

NS_AFTER_START = 1500000000

def appendReadings(playerReadings, packet):
    playerReadings[0].append(packet[beetles.ACCEL_X])
    playerReadings[1].append(packet[beetles.ACCEL_Y])
    playerReadings[2].append(packet[beetles.ACCEL_Z])
    playerReadings[3].append(packet[beetles.ROTATE_X])
    playerReadings[4].append(packet[beetles.ROTATE_Y])
    playerReadings[5].append(packet[beetles.ROTATE_Z])

def getProcessedData(readings):
    processedData = []
    for i in range(len(readings)):
        processedData.append(statistics.mean(readings[i]))
        processedData.append(max(readings[i]) - min(readings[i]))
        processedData.append(statistics.pvariance(readings[i]))
        processedData.append(statistics.median(readings[i]))
    return processedData

def getMaxAbsSecondDerivative(data):
    return max(abs((data[i + 2] - data[i + 1]) - (data[i + 1] - data[i])) for i in range(len(data) - 2))

class MoveClassifier:
    def __init__(self):
        self.overlay = Overlay('design_1.bit')
        self.dma = self.overlay.axi_dma_0
        self.dma_send = self.overlay.axi_dma_0.sendchannel
        self.dma_recv = self.overlay.axi_dma_0.recvchannel

        self.input_buffer = allocate(shape=(24,), dtype = np.float32)
        self.output_buffer = allocate(shape=(5,), dtype = np.float32)

    # data here is already processed
    def classifyMove(self, data):
        self.input_buffer[:] = data

        self.dma_send.transfer(self.input_buffer)
        self.dma_recv.transfer(self.output_buffer)

        self.dma_send.wait()
        self.dma_recv.wait()
        idx = self.output_buffer.argmax(axis=0) + 1
        # print("move engine got index", idx)
        return INDEX_TO_ACTION_MAP[idx]

    # data here is raw
    def isStartOfMove(self, prevAccelY, currAccelY):
        return currAccelY - prevAccelY > 1000

def startMoveProcess(actionQueue: mp.Queue, beetleQueue: mp.Queue):

    classifier = MoveClassifier()

    while True:
        p1Move, p2Move, didP1GetShot, didP2GetShot = getMoves(beetleQueue, classifier)
        print("move process got:", p1Move, p2Move, didP1GetShot, didP2GetShot)

        if p1Move != Actions.no or p2Move != Actions.no:
            actionQueue.put((p1Move, p2Move, didP1GetShot, didP2GetShot), block=True)

def getMoves(beetleQueue: mp.Queue, classifier: MoveClassifier):
    p1Move = Actions.no
    p2Move = Actions.no

    didP1GetShot = False
    didP2GetShot = False

    hasP1WristMoved = False
    p1WristStartTime = None
    hasP2WristMoved = False
    p2WristStartTime = None

    p1Readings = [[] for _ in range(6)]
    p2Readings = [[] for _ in range(6)]

    prevP1AccelY = 0
    prevP2AccelY = 0

    while (p1Move == Actions.no and p2Move == Actions.no):

        packet = beetleQueue.get(block = True)
        beetleID = packet[beetles.PACKET_TYPE]

        if beetleID == beetles.P1_GUN:
            p1Move = Actions.shoot

        elif beetleID == beetles.P1_VEST:
            didP1GetShot = True

        elif beetleID == beetles.P1_WRIST:
            if hasP1WristMoved:
                appendReadings(p1Readings, packet)
                if time.time_ns() - p1WristStartTime >= NS_AFTER_START:
                    print("length of raw p1 readings:", len(p1Readings[0]))
                    p1WristData = getProcessedData(p1Readings)
                    print("length of processed p1 readings:", len(p1WristData))
                    if len(p1WristData):
                        p1Move = classifier.classifyMove(p1WristData)
            
            else:
                if classifier.isStartOfMove(prevP1AccelY, packet[beetles.ACCEL_Y]):
                    hasP1WristMoved = True
                    appendReadings(p1Readings, packet)
                    p1WristStartTime = time.time_ns()
                else:
                    prevP1AccelY = packet[beetles.ACCEL_Y]

        elif beetleID == beetles.P2_GUN:
            p2Move = Actions.shoot

        elif beetleID == beetles.P2_VEST:
            didP2GetShot = True

        elif beetleID == beetles.P2_WRIST:
            if hasP2WristMoved:
                appendReadings(p2Readings, packet)
                if time.time_ns() - p2WristStartTime >= NS_AFTER_START:
                    print("length of raw p2 readings:", len(p2Readings[0]))
                    p2WristData = getProcessedData(p2Readings)
                    print("length of processed p2 readings:", len(p2WristData))
                    if len(p2WristData):
                        p2Move = classifier.classifyMove(p2WristData)

            else:
                if classifier.isStartOfMove(prevP2AccelY, packet[beetles.ACCEL_Y]):
                    hasP2WristMoved = True
                    appendReadings(p2Readings, packet)
                    p2WristStartTime = time.time_ns()
                else:
                    prevP2AccelY = packet[beetles.ACCEL_Y]


    return p1Move, p2Move, didP1GetShot, didP2GetShot
