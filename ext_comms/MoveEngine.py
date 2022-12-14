import multiprocessing as mp
import statistics
import time as time
import warnings

import joblib
import numpy as np
import pandas as pd
from pynq import Overlay, allocate
from sklearn.preprocessing import StandardScaler

import BeetleMain as beetles
from Player import Actions

INDEX_TO_ACTION_MAP = {1: "grenade", 2: "reload", 3: "shield", 4: "logout", 5: "reload"}

NS_AFTER_START = 2000000000
NS_AFTER_DOUBLESHOOT = 100000000
MIN_READINGS_NEEDED = 25

p1NumSamples = 0
p2NumSamples = 0

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
        processedData.append(max(readings[i]))
        processedData.append(min(readings[i]))
        processedData.append(statistics.pvariance(readings[i], processedData[0]))
        processedData.append(statistics.median(readings[i]))
        processedData.append(np.percentile(readings, 25))
        processedData.append(np.percentile(readings, 75))
    return processedData

class MoveClassifier:
    def __init__(self):
        self.overlay = Overlay('design_1_10nov.bit')
        self.dma = self.overlay.axi_dma_0
        self.dma_send = self.overlay.axi_dma_0.sendchannel
        self.dma_recv = self.overlay.axi_dma_0.recvchannel

        self.input_buffer = allocate(shape=(42,), dtype = np.float32)
        self.output_buffer = allocate(shape=(5,), dtype = np.float32)

        self.scaler = joblib.load('scaler.joblib')
        warnings.filterwarnings("ignore")

    # data here is already processed
    def classifyMove(self, data):

        scaled_data = self.scaler.transform(np.array(data).reshape(1, -1))

        self.input_buffer[:] = scaled_data

        self.dma_send.transfer(self.input_buffer)
        self.dma_recv.transfer(self.output_buffer)

        self.dma_send.wait()
        self.dma_recv.wait()
        idx = self.output_buffer.argmax(axis=0) + 1
        return INDEX_TO_ACTION_MAP[idx]

    # data here is raw
    def isStartOfMove(self, prevAccelY, currAccelY):
        return currAccelY - prevAccelY > 1000

def startMoveProcess(actionQueue: mp.Queue, beetleQueue: mp.Queue):

    classifier = MoveClassifier()

    while True:
        p1Move, p2Move, didP1GetShot, didP2GetShot = getMoves(beetleQueue, classifier)

        if p1Move != Actions.no or p2Move != Actions.no:
            actionQueue.put((p1Move, p2Move, didP1GetShot, didP2GetShot), block=True)

def getMoves(beetleQueue: mp.Queue, classifier: MoveClassifier):

    global p1NumSamples, p2NumSamples
    p1Move = Actions.no
    p2Move = Actions.no

    didP1GetShot = False
    didP2GetShot = False

    hasP1WristMoved = False
    p1WristStartTime = None
    hasP2WristMoved = False
    p2WristStartTime = None

    hasP1WristProcessed = False
    hasP2WristProcessed = False

    p1Readings = [[] for _ in range(6)]
    p2Readings = [[] for _ in range(6)]

    prevP1AccelY = 0
    prevP2AccelY = 0

    start = time.time_ns()
    print("sleeping...")
    while time.time_ns() - start < 500000000:
        packet = beetleQueue.get(block = True)
    print("ready!")

    while (p1Move == Actions.no or p2Move == Actions.no):

        packet = beetleQueue.get(block = True)
        beetleID = packet[beetles.PACKET_TYPE]

        if beetleID == beetles.P1_GUN:
            p1Move = Actions.shoot

        elif beetleID == beetles.P1_VEST:
            didP1GetShot = True

        elif beetleID == beetles.P1_WRIST and not hasP1WristProcessed:
            if hasP1WristMoved:
                appendReadings(p1Readings, packet)
                if len(p1Readings[0]) >= MIN_READINGS_NEEDED or time.time_ns() - p1WristStartTime >= NS_AFTER_START:
                    print("length of raw p1 readings:", len(p1Readings[0]))
                    p1WristData = getProcessedData(p1Readings)

                    if len(p1WristData):
                        p1Move = classifier.classifyMove(p1WristData)
                        hasP1WristProcessed = True
            
            else:
                if classifier.isStartOfMove(prevP1AccelY, packet[beetles.ACCEL_Y]):
                    hasP1WristMoved = True
                    print("p1 start of move detected")
                    appendReadings(p1Readings, packet)
                    p1WristStartTime = time.time_ns()
                else:
                    prevP1AccelY = packet[beetles.ACCEL_Y]

        elif beetleID == beetles.P2_GUN:
            p2Move = Actions.shoot

        elif beetleID == beetles.P2_VEST:
            didP2GetShot = True

        elif beetleID == beetles.P2_WRIST and not hasP2WristProcessed:
            if hasP2WristMoved:
                appendReadings(p2Readings, packet)
                if len(p2Readings[0]) >= MIN_READINGS_NEEDED or time.time_ns() - p2WristStartTime >= NS_AFTER_START:
                    print("length of raw p2 readings:", len(p2Readings[0]))
                    p2WristData = getProcessedData(p2Readings)

                    if len(p2WristData):
                        p2Move = classifier.classifyMove(p2WristData)
                        hasP2WristProcessed = True

            else:
                if classifier.isStartOfMove(prevP2AccelY, packet[beetles.ACCEL_Y]):
                    print("p2 start of move detected")
                    hasP2WristMoved = True
                    appendReadings(p2Readings, packet)
                    p2WristStartTime = time.time_ns()
                else:
                    prevP2AccelY = packet[beetles.ACCEL_Y]

    if p1Move == Actions.shoot and p2Move == Actions.shoot:
        waitForVestStartTime = time.time_ns()
        while time.time_ns() <= waitForVestStartTime + NS_AFTER_DOUBLESHOOT:
            packet = beetleQueue.get(block = True)
            beetleID = packet[beetles.PACKET_TYPE]

            if beetleID == beetles.P1_VEST:
                didP1GetShot = True

            elif beetleID == beetles.P2_VEST:
                didP2GetShot = True

    return p1Move, p2Move, didP1GetShot, didP2GetShot
