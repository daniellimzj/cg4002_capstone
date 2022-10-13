import multiprocessing as mp
import statistics
import time as time

import numpy as np
import pandas as pd
from pynq import Overlay, allocate

import BeetleMain as beetles
from Player import Actions

INDEX_TO_ACTION_MAP = {1: "grenade", 2: "reload", 3: "shield", 4: "logout", 5: "none"}

NS_AFTER_THRESHOLD = 1900000000

def appendReadings(playerReadings, packet):
    playerReadings[0].append(packet[beetles.ACCEL_X])
    playerReadings[1].append(packet[beetles.ACCEL_Y])
    playerReadings[2].append(packet[beetles.ACCEL_Z])
    playerReadings[3].append(packet[beetles.ROTATE_X])
    playerReadings[4].append(packet[beetles.ROTATE_Y])
    playerReadings[5].append(packet[beetles.ROTATE_Z])

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
    def isStartOfMove(self, rawData):
        return rawData[beetles.ACCEL_Y] > -12000 or rawData[beetles.ACCEL_Y] < -20000

def startMoveProcess(actionQueue: mp.Queue, beetleQueue: mp.Queue):

    classifier = MoveClassifier()

    while True:
        p1Move, p2Move, didP1GetShot, didP2GetShot = getMoves(beetleQueue, classifier)

        if p1Move != Actions.no or p2Move != Actions.no:
            actionQueue.put((p1Move, p2Move, didP1GetShot, didP2GetShot), block=True)

def getMoves(beetleQueue: mp.Queue, classifier: MoveClassifier):
    p1Move = Actions.no
    p2Move = Actions.no

    didP1GetShot = False
    didP2GetShot = False

    gotPacketFromP1Wrist = False
    gotPacketFromP2Wrist = False

    p1Readings = [[] for _ in range(6)]
    p2Readings = [[] for _ in range(6)]

    packet = beetleQueue.get(block = True)
    beetleID = packet[beetles.PACKET_TYPE]

    while (beetleID == beetles.P1_WRIST and not classifier.isStartOfMove(packet)) or (beetleID == beetles.P2_WRIST and not classifier.isStartOfMove(packet)):
        packet = beetleQueue.get(block = True)
        beetleID = packet[beetles.PACKET_TYPE]

    print("packet has passed the test, id:", beetleID)
    startTime = time.time_ns()

    if beetleID == beetles.P1_WRIST:
        appendReadings(p1Readings, packet)
        gotPacketFromP1Wrist = True

    elif beetleID == beetles.P2_WRIST:
        appendReadings(p2Readings, packet)
        gotPacketFromP2Wrist = True

    elif beetleID == beetles.P1_GUN:
        p1Move = Actions.shoot

    elif beetleID == beetles.P2_GUN:
        p2Move = Actions.shoot

    elif beetleID == beetles.P1_VEST:
        didP1GetShot = True
            
    elif beetleID == beetles.P2_VEST:
        didP2GetShot = True 

    while time.time_ns() - startTime < NS_AFTER_THRESHOLD:
        try:
            packet = beetleQueue.get(block = False, timeout=None)
            beetleID = packet[beetles.PACKET_TYPE]

            if beetleID == beetles.P1_WRIST:
                appendReadings(p1Readings, packet)
                gotPacketFromP1Wrist = True

            elif beetleID == beetles.P2_WRIST:
                appendReadings(p2Readings, packet)
                gotPacketFromP2Wrist = True

            elif beetleID == beetles.P1_GUN:
                print("in", "{:.3f}".format(NS_AFTER_THRESHOLD / 1000000000),"second, got", beetleID)
                p1Move = Actions.shoot

            elif beetleID == beetles.P2_GUN:
                print("in", "{:.3f}".format(NS_AFTER_THRESHOLD / 1000000000),"second, got", beetleID)
                p2Move = Actions.shoot

            elif beetleID == beetles.P1_VEST:
                print("in", "{:.3f}".format(NS_AFTER_THRESHOLD / 1000000000),"second, got", beetleID)
                didP1GetShot = True
            
            elif beetleID == beetles.P2_VEST:
                print("in", "{:.3f}".format(NS_AFTER_THRESHOLD / 1000000000),"second, got", beetleID)
                didP2GetShot = True       

        except:
            continue

    if p1Move != Actions.shoot and gotPacketFromP1Wrist:
        p1WristData = []
        print("length of readings:", len(p1WristData))
        for i in range(len(p1Readings)):
            p1WristData.append(statistics.mean(p1Readings[i]))
            p1WristData.append(max(p1Readings[i]) - min(p1Readings[i]))
            p1WristData.append(statistics.pvariance(p1Readings[i]))
            p1WristData.append(statistics.median(p1Readings[i]))
        if len(p1WristData):
            p1Move = classifier.classifyMove(p1WristData)

    if p2Move != Actions.shoot and gotPacketFromP2Wrist:
        p2WristData = []
        for i in range(len(p2Readings)):
            p1WristData.append(statistics.mean(p2Readings[i]))
            p1WristData.append(max(p2Readings[i]) - min(p2Readings[i]))
            p1WristData.append(statistics.pvariance(p2Readings[i]))
            p1WristData.append(statistics.median(p2Readings[i]))
        if len(p2WristData):
            p2Move = classifier.classifyMove(p2WristData)

    print("getMoves now returning",p1Move, p2Move, didP1GetShot, didP2GetShot)
    return p1Move, p2Move, didP1GetShot, didP2GetShot
