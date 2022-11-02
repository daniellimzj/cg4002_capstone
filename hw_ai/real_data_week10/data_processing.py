import os
import numpy as np
from statistics import mean, pvariance, median

folder = os.getcwd() + "\\data"
extracted_folder = folder + "\\extracted"
actions = ["grenade", "reload", "shield", "newend"]
key = {"grenade": 1, "reload": 2, "shield": 3, "newend": 4}
raw_features = ["accX", "accY", "accZ", "gyroX", "gyroY", "gyroZ"]
extracted_features = ["mean", "max", "min", "var", "median", "25thp", "75thp"]


def getStats(parameter):
    avg = mean(parameter)
    med = median(parameter)
    var = pvariance(parameter)
    maximum = max(parameter)
    minimum = min(parameter)
    iqrLower = np.percentile(parameter, 25)
    iqrUpper = np.percentile(parameter, 75)
    return avg, maximum, minimum, var, med, iqrLower, iqrUpper


def generateHeader():
    header = ''
    for i in range(len(raw_features)):
        for j in range(len(extracted_features)):
            header = header + extracted_features[j] + raw_features[i] + ","

    return header + 'label'


def main():
    for file in os.listdir(folder):
        if ([action for action in actions if (action in file)]) and "extracted" not in file:
            action = file.replace(".txt", "")
            action = file.split("_")[0]
            name = file.split("_")[1]
            f = open(folder + "\\" + file, "r")
            f2 = open(extracted_folder + "\\" + "extracted_" + file, "a+")
            lines = f.readlines()
            count = 0
            accX = []
            accY = []
            accZ = []
            gyroX = []
            gyroY = []
            gyroZ = []

            for line in lines:
                count += 1
                if count % 38 > 0:
                    if count % 26 > 0:
                        line = line.strip()
                        result = line.split(",")
                        component = [eval(i) for i in result]
                        accX.append(component[0])
                        accY.append(component[1])
                        accZ.append(component[2])
                        gyroX.append(component[3])
                        gyroY.append(component[4])
                        gyroZ.append(component[5])
                elif count != 0:
                    meanaccX, maxaccX, minaccX, varaccX, medaccX, iqrLoweraccX, iqrUpperaccX = getStats(accX)
                    meanaccY, maxaccY, minaccY, varaccY, medaccY, iqrLoweraccY, iqrUpperaccY = getStats(accY)
                    meanaccZ, maxaccZ, minaccZ, varaccZ, medaccZ, iqrLoweraccZ, iqrUpperaccZ = getStats(accZ)
                    meangyroX, maxgyroX, mingyroX, vargyroX, medgyroX, iqrLowergyroX, iqrUppergyroX = getStats(gyroX)
                    meangyroY, maxgyroY, mingyroY, vargyroY, medgyroY, iqrLowergyroY, iqrUppergyroY = getStats(gyroY)
                    meangyroZ, maxgyroZ, mingyroZ, vargyroZ, medgyroZ, iqrLowergyroZ, iqrUppergyroZ = getStats(gyroZ)

                    f2.write(str(meanaccX) + "," + str(maxaccX) + "," + str(minaccX) + "," + str(varaccX) + "," + str(medaccX) + "," + str(iqrLoweraccX) + "," + str(iqrUpperaccX) + ",")
                    f2.write(str(meanaccY) + "," + str(maxaccY) + "," + str(minaccY) + "," + str(varaccY) + "," + str(medaccY) + "," + str(iqrLoweraccY) + "," + str(iqrUpperaccY) + ",")
                    f2.write(str(meanaccZ) + "," + str(maxaccZ) + "," + str(minaccZ) + "," + str(varaccZ) + "," + str(medaccZ) + "," + str(iqrLoweraccZ) + "," + str(iqrUpperaccZ) + ",")
                    f2.write(str(meangyroX) + "," + str(maxgyroX) + "," + str(mingyroX) + "," + str(vargyroX) + "," + str(medgyroX) + "," + str(iqrLowergyroX) + "," + str(iqrUppergyroX) + ",")
                    f2.write(str(meangyroY) + "," + str(maxgyroY) + "," + str(mingyroY) + "," + str(vargyroY) + "," + str(medgyroY) + "," + str(iqrLowergyroY) + "," + str(iqrUppergyroY) + ",")

                    if count != len(lines):
                        f2.write(str(meangyroZ) + "," + str(maxgyroZ) + "," + str(mingyroZ) + "," + str(
                            vargyroZ) + "," + str(medgyroZ) + "," + str(iqrLowergyroZ) + "," + str(iqrUppergyroZ) + "," + str(key[action]) + "\n")
                    else:
                        f2.write(str(meangyroZ) + "," + str(maxgyroZ) + "," + str(mingyroZ) + "," + str(
                            vargyroZ) + "," + str(medgyroZ) + "," + str(iqrLowergyroZ) + "," + str(iqrUppergyroZ) + "," + str(key[action]))
                    accX.clear()
                    accY.clear()
                    accZ.clear()
                    gyroX.clear()
                    gyroY.clear()
                    gyroZ.clear()
            f2.close()

    csv_f = open("main.csv", "w+")
    header_string = generateHeader()
    csv_f.write(header_string + "\n")

    for file in os.listdir(extracted_folder):
        if "extracted" in file:
            print("processing: " + file)
            file_handler = open(extracted_folder + "\\" + file, "r")
            ls = file_handler.readlines()
            for line in ls:
                csv_f.write(line)
            csv_f.write("\n")


if __name__ == "__main__":
    main()
