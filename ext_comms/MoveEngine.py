import multiprocessing as mp
import statistics
import time as time

import joblib
import numpy as np
import pandas as pd
from pynq import Overlay, allocate
from sklearn.preprocessing import StandardScaler

import BeetleMain as beetles
from Player import Actions

INDEX_TO_ACTION_MAP = {1: "grenade", 2: "reload", 3: "shield", 4: "logout", 5: "none"}

NS_AFTER_START = 1500000000

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
        self.overlay = Overlay('design_1_31oct.bit')
        self.dma = self.overlay.axi_dma_0
        self.dma_send = self.overlay.axi_dma_0.sendchannel
        self.dma_recv = self.overlay.axi_dma_0.recvchannel

        self.input_buffer = allocate(shape=(42,), dtype = np.float32)
        self.output_buffer = allocate(shape=(5,), dtype = np.float32)

        self.scaler = joblib.load('scaler.joblib')

        # testData = [5387.923076923077,12007,-7691,32407388.737672586,7462,2745.5,9614.0,-9195.692307692309,-4802,-14923,11716324.520710059,-8048,-12456.0,-6344.5,-1085.4102564102564,5792,-13853,46926777.318869166,3200,-7126.5,4584.0,-11869.846153846154,-3129,-23751,37783929.77120315,-9640,-16942.5,-7670.0,-1844.051282051282,4205,-11429,16273600.151216306,-1659,-4385.5,968.5,1678.3589743589744,17484,-19211,144046643.15318868,5518,-10452.0,10139.0]

        # testDataScaled = self.scaler.transform(np.array(testData).reshape(1, -1))

        # print(testDataScaled)


    # data here is already processed
    def classifyMove(self, data):

        scaled_data = self.scaler.transform(np.array(data).reshape(1, -1))

        self.input_buffer[:] = scaled_data

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
                if time.time_ns() - p1WristStartTime >= NS_AFTER_START:
                    print("length of raw p1 readings:", len(p1Readings[0]))
                    p1WristData = getProcessedData(p1Readings)

                    start = time.time_ns()
                    p1NumSamples += 1
                    with open("p1_wrist_" + f'{p1NumSamples:04}' + ".txt", "w") as file:
                        for i in range(len(p1Readings[0])):
                            file.write(",".join(str(p1Readings[j][i]) for j in range(6)))
                            file.write("\n")
                    print("milliseconds taken to write p1 samples to file:", (time.time_ns() - start) / 1000000)

                    if len(p1WristData):
                        start = time.time_ns()
                        p1Move = classifier.classifyMove(p1WristData)
                        hasP1WristProcessed = True
                        print("milliseconds taken to classify p2 move:", (time.time_ns() - start) / 1000000)
            
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
                if time.time_ns() - p2WristStartTime >= NS_AFTER_START:
                    print("length of raw p2 readings:", len(p2Readings[0]))
                    p2WristData = getProcessedData(p2Readings)

                    start = time.time_ns()
                    p2NumSamples += 1
                    with open("p2_wrist_" + f'{p2NumSamples:04}' + ".txt", "w") as file:
                        for i in range(len(p2Readings[0])):
                            file.write(",".join(str(p2Readings[j][i]) for j in range(6)))
                            file.write("\n")
                    print("milliseconds taken to write p2 samples to file:", (time.time_ns() - start) / 1000000)

                    if len(p2WristData):
                        start = time.time_ns()
                        p2Move = classifier.classifyMove(p2WristData)
                        hasP2WristProcessed = True
                        print("milliseconds taken to classify p2 move:", (time.time_ns() - start) / 1000000)

            else:
                if classifier.isStartOfMove(prevP2AccelY, packet[beetles.ACCEL_Y]):
                    print("p2 start of move detected")
                    hasP2WristMoved = True
                    appendReadings(p2Readings, packet)
                    p2WristStartTime = time.time_ns()
                else:
                    prevP2AccelY = packet[beetles.ACCEL_Y]


    return p1Move, p2Move, didP1GetShot, didP2GetShot
