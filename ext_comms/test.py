import numpy as np
import statistics
import time


readings = [[] for _ in range(6)]


def appendReadings(playerReadings, packet):
    playerReadings[0].append(packet[0])
    playerReadings[1].append(packet[1])
    playerReadings[2].append(packet[2])
    playerReadings[3].append(packet[3])
    playerReadings[4].append(packet[4])
    playerReadings[5].append(packet[5])

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

with open("data_collection_irl_27oct/p1_grenade0003.txt", "r") as file:
    for line in file:
        packet = line.split(",")
        appendReadings(readings, [int(i) for i in line.split(",")])

print(len(readings), len(readings[0]))

start = time.time_ns()
print("Asdfasdfasdfasdfasdfasdfasd", start, len(readings))
print((time.time_ns() - start) / 1000000)



