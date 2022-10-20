import os
from statistics import mean, variance, median

folder = "C:\\Users\\yh\\Documents\\GitHub\\cg4002_capstone\\hw_ai\\real_data_week10\\data"
actions = ["grenade", "reload", "shield", "end"]
key = {"grenade": 1, "reload": 2, "shield": 3, "end": 4}


def getStats(parameter):
    avg = mean(parameter)
    med = median(parameter)
    var = variance(parameter)
    rg = max(parameter) - min(parameter)
    return avg, rg, var, med


def main():
    for file in os.listdir(folder):
        # if ([action for action in actions if (action in file)]) and "extracted" not in file:
         if file == "test.txt":
            print(file)
            # action = file.replace(".txt", "")
            # action = file.split("_")[0]
            # name = file.split("_")[1]
            action = "grenade"
            f = open(file, "r")
            f2 = open("extracted_" + file, "a+")
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
                    meanaccX, rgaccX, varaccX, medaccX = getStats(accX)
                    meanaccY, rgaccY, varaccY, medaccY = getStats(accY)
                    meanaccZ, rgaccZ, varaccZ, medaccZ = getStats(accZ)
                    meangyroX, rggyroX, vargyroX, medgyroX = getStats(gyroX)
                    meangyroY, rggyroY, vargyroY, medgyroY = getStats(gyroY)
                    meangyroZ, rggyroZ, vargyroZ, medgyroZ = getStats(gyroZ)
                    f2.write(str(meanaccX) + "," + str(rgaccX) + "," + str(varaccX) + "," + str(medaccX) + ",")
                    f2.write(str(meanaccY) + "," + str(rgaccY) + "," + str(varaccY) + "," + str(medaccY) + ",")
                    f2.write(str(meanaccZ) + "," + str(rgaccZ) + "," + str(varaccZ) + "," + str(medaccZ) + ",")
                    f2.write(str(meangyroX) + "," + str(rggyroX) + "," + str(vargyroX) + "," + str(medgyroX) + ",")
                    f2.write(str(meangyroY) + "," + str(rggyroY) + "," + str(vargyroY) + "," + str(medgyroY) + ",")
                    if count != len(lines):
                        f2.write(str(meangyroZ) + "," + str(rggyroZ) + "," + str(vargyroZ) + "," + str(medgyroZ) + "," + str(key[action]) + "\n")
                    else:
                        f2.write(str(meangyroZ) + "," + str(rggyroZ) + "," + str(vargyroZ) + "," + str(medgyroZ) + "," + str(key[action]))
                    accX.clear()
                    accY.clear()
                    accZ.clear()
                    gyroX.clear()
                    gyroY.clear()
                    gyroZ.clear()
            f2.close()
    ef0 = open(folder + "\\extracted_test.txt", "r")
    # ef1 = open(folder + "\\extracted_grenade_yh.txt", "r")
    # ef2 = open(folder + "\\extracted_reload_yh.txt", "r")
    # ef3 = open(folder + "\\extracted_shield_yh.txt", "r")
    # ef4 = open(folder + "\\extracted_end_yh.txt", "r")
    # ef5 = open(folder + "\\extracted_grenade_jm.txt", "r")
    # ef6 = open(folder + "\\extracted_reload_jm.txt", "r")
    # ef7 = open(folder + "\\extracted_shield_jm.txt", "r")
    # ef8 = open(folder + "\\extracted_end_jm.txt", "r")
    # ef9 = open(folder + "\\extracted_grenade_bryan.txt", "r")
    # ef10 = open(folder + "\\extracted_reload_bryan.txt", "r")
    # ef11 = open(folder + "\\extracted_shield_bryan.txt", "r")
    # ef12 = open(folder + "\\extracted_end_bryan.txt", "r")
    # ef13 = open(folder + "\\extracted_grenade_rebecca.txt", "r")
    # ef14 = open(folder + "\\extracted_reload_rebecca.txt", "r")
    # ef15 = open(folder + "\\extracted_shield_rebecca.txt", "r")
    # ef16 = open(folder + "\\extracted_end_rebecca.txt", "r")
    # ef17 = open(folder + "\\extracted_grenade_daniel.txt", "r")
    # ef18 = open(folder + "\\extracted_reload_daniel.txt", "r")
    # ef19 = open(folder + "\\extracted_shield_daniel.txt", "r")
    # ef20 = open(folder + "\\extracted_end_daniel.txt", "r")

    csv_f = open("test_main.csv", "w+")
    header_string = "Mean-accX,Range-accX,Var-accX,Median-accX,Mean-accY,Range-accY,Var-accY,Median-accY,Mean-accZ,Range-accZ,Var-accZ,Median-accZ,Mean-gyroX,Range-gyroX,Var-gyroX,Median-gyroX,Mean-gyroY,Range-gyroY,Var-gyroY,Median-gyroY,Mean-gyroZ,Range-gyroZ,Var-gyroZ,Median-gyroZ,label"
    csv_f.write(header_string + "\n")

    ls0 = ef0.readlines()
    for line in ls0:
        csv_f.write(line)
    csv_f.write("\n")

    # ls1 = ef1.readlines()
    # for line in ls1:
    #     csv_f.write(line)
    # csv_f.write("\n")
    #
    # ls2 = ef2.readlines()
    # for line in ls2:
    #     csv_f.write(line)
    # csv_f.write("\n")
    #
    # ls3 = ef3.readlines()
    # for line in ls3:
    #     csv_f.write(line)
    # csv_f.write("\n")
    #
    # ls4 = ef4.readlines()
    # for line in ls4:
    #     csv_f.write(line)
    # csv_f.write("\n")
    #
    # ls5 = ef5.readlines()
    # for line in ls5:
    #     csv_f.write(line)
    # csv_f.write("\n")
    #
    # ls6 = ef6.readlines()
    # for line in ls6:
    #     csv_f.write(line)
    # csv_f.write("\n")
    #
    # ls7 = ef7.readlines()
    # for line in ls7:
    #     csv_f.write(line)
    # csv_f.write("\n")
    #
    # ls8 = ef8.readlines()
    # for line in ls8:
    #     csv_f.write(line)
    # csv_f.write("\n")
    #
    # ls9 = ef9.readlines()
    # for line in ls9:
    #     csv_f.write(line)
    # csv_f.write("\n")
    #
    # ls10 = ef10.readlines()
    # for line in ls10:
    #     csv_f.write(line)
    # csv_f.write("\n")
    #
    # ls11 = ef11.readlines()
    # for line in ls11:
    #     csv_f.write(line)
    # csv_f.write("\n")
    #
    # ls12 = ef12.readlines()
    # for line in ls12:
    #     csv_f.write(line)
    # csv_f.write("\n")
    #
    # ls13 = ef13.readlines()
    # for line in ls13:
    #     csv_f.write(line)
    # csv_f.write("\n")
    #
    # ls14 = ef14.readlines()
    # for line in ls14:
    #     csv_f.write(line)
    # csv_f.write("\n")
    #
    # ls15 = ef15.readlines()
    # for line in ls15:
    #     csv_f.write(line)
    # csv_f.write("\n")
    #
    # ls16 = ef16.readlines()
    # for line in ls16:
    #     csv_f.write(line)
    # csv_f.write("\n")
    #
    # ls17 = ef17.readlines()
    # for line in ls17:
    #     csv_f.write(line)
    # csv_f.write("\n")
    #
    # ls18 = ef18.readlines()
    # for line in ls18:
    #     csv_f.write(line)
    # csv_f.write("\n")
    #
    # ls19 = ef19.readlines()
    # print(ls19)
    # for line in ls19:
    #     csv_f.write(line)
    # csv_f.write("\n")
    #
    # ls20 = ef20.readlines()
    # for line in ls20:
    #     csv_f.write(line)
    # csv_f.write("\n")


if __name__ == "__main__":
    main()