import numpy as np
import statistics
import time
import joblib
from sklearn.preprocessing import StandardScaler



# readings = [[] for _ in range(6)]


# def appendReadings(playerReadings, packet):
#     playerReadings[0].append(packet[0])
#     playerReadings[1].append(packet[1])
#     playerReadings[2].append(packet[2])
#     playerReadings[3].append(packet[3])
#     playerReadings[4].append(packet[4])
#     playerReadings[5].append(packet[5])

# def getProcessedData(readings):
#     processedData = []
#     for i in range(len(readings)):
#         processedData.append(statistics.mean(readings[i]))
#         processedData.append(max(readings[i]))
#         processedData.append(min(readings[i]))
#         processedData.append(statistics.pvariance(readings[i], processedData[0]))
#         processedData.append(statistics.median(readings[i]))
#         processedData.append(np.percentile(readings, 25))
#         processedData.append(np.percentile(readings, 75))
#     return processedData

# with open("data_collection_irl_27oct/p1_grenade0003.txt", "r") as file:
#     for line in file:
#         packet = line.split(",")
#         appendReadings(readings, [int(i) for i in line.split(",")])

# print(len(readings), len(readings[0]))

# start = time.time_ns()
# print("Asdfasdfasdfasdfasdfasdfasd", start, len(readings))
# print((time.time_ns() - start) / 1000000)

scaler = joblib.load('scaler.joblib')

testData = np.array([5387.923076923077,12007,-7691,32407388.737672586,7462,2745.5,9614.0,-9195.692307692309,-4802,-14923,11716324.520710059,-8048,-12456.0,-6344.5,-1085.4102564102564,5792,-13853,46926777.318869166,3200,-7126.5,4584.0,-11869.846153846154,-3129,-23751,37783929.77120315,-9640,-16942.5,-7670.0,-1844.051282051282,4205,-11429,16273600.151216306,-1659,-4385.5,968.5,1678.3589743589744,17484,-19211,144046643.15318868,5518,-10452.0,10139.0])

testDataScaled = scaler.transform(testData.reshape(1, -1))

print(testDataScaled)




