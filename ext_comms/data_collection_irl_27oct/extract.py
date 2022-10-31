import os
import numpy as np
from statistics import mean, pvariance, median

folder = "D:\\CG4002\\cg4002_capstone\\ext_comms\\data_collection_irl_27oct"


def getStats(parameter):
    avg = mean(parameter)
    med = median(parameter)
    var = pvariance(parameter)
    maximum = max(parameter)
    minimum = min(parameter)
    iqrLower = np.percentile(parameter, 25)
    iqrUpper = np.percentile(parameter, 75)
    return avg, maximum, minimum, var, med, iqrLower, iqrUpper


for file in os.listdir(folder):
    f2 = open(folder + "\\" + "extracted.txt", "a+")
    if "extracted" not in file and ".txt" in file:
        accX = []
        accY = []
        accZ = []
        gyroX = []
        gyroY = []
        gyroZ = []
        action = file.split('_')[1]
        if "grenade" in action:
            action = 1
        elif "reload" in action:
            action = 2
        elif "shield" in action:
            action = 3
        elif "logout" in action:
            action = 4

        f = open(folder + "\\" + file, "r")
        lines = f.readlines()
        for line in lines:
            result = line.split(",")
            component = [eval(i) for i in result]
            accX.append(component[0])
            accY.append(component[1])
            accZ.append(component[2])
            gyroX.append(component[3])
            gyroY.append(component[4])
            gyroZ.append(component[5])
        meanaccX, maxaccX, minaccX, varaccX, medaccX, iqrLoweraccX, iqrUpperaccX = getStats(accX)
        meanaccY, maxaccY, minaccY, varaccY, medaccY, iqrLoweraccY, iqrUpperaccY = getStats(accY)
        meanaccZ, maxaccZ, minaccZ, varaccZ, medaccZ, iqrLoweraccZ, iqrUpperaccZ = getStats(accZ)
        meangyroX, maxgyroX, mingyroX, vargyroX, medgyroX, iqrLowergyroX, iqrUppergyroX = getStats(gyroX)
        meangyroY, maxgyroY, mingyroY, vargyroY, medgyroY, iqrLowergyroY, iqrUppergyroY = getStats(gyroY)
        meangyroZ, maxgyroZ, mingyroZ, vargyroZ, medgyroZ, iqrLowergyroZ, iqrUppergyroZ = getStats(gyroZ)

        f2.write(str(meanaccX) + "," + str(maxaccX) + "," + str(minaccX) + "," + str(varaccX) + "," + str(
            medaccX) + "," + str(iqrLoweraccX) + "," + str(iqrUpperaccX) + ",")
        f2.write(str(meanaccY) + "," + str(maxaccY) + "," + str(minaccY) + "," + str(varaccY) + "," + str(
            medaccY) + "," + str(iqrLoweraccY) + "," + str(iqrUpperaccY) + ",")
        f2.write(str(meanaccZ) + "," + str(maxaccZ) + "," + str(minaccZ) + "," + str(varaccZ) + "," + str(
            medaccZ) + "," + str(iqrLoweraccZ) + "," + str(iqrUpperaccZ) + ",")
        f2.write(str(meangyroX) + "," + str(maxgyroX) + "," + str(mingyroX) + "," + str(vargyroX) + "," + str(
            medgyroX) + "," + str(iqrLowergyroX) + "," + str(iqrUppergyroX) + ",")
        f2.write(str(meangyroY) + "," + str(maxgyroY) + "," + str(mingyroY) + "," + str(vargyroY) + "," + str(
            medgyroY) + "," + str(iqrLowergyroY) + "," + str(iqrUppergyroY) + ",")
        f2.write(str(meangyroZ) + "," + str(maxgyroZ) + "," + str(mingyroZ) + "," + str(
            vargyroZ) + "," + str(medgyroZ) + "," + str(iqrLowergyroZ) + "," + str(iqrUppergyroZ) + "," + str(
            action) + "\n")
