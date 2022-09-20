import statistics
import random

for i in range(6):

    arr = [(i + 1) * (j + 1) for j in range(10)]

    print(arr)
    print("Mean: ", "{:.2f}".format(statistics.mean(arr)))
    print("Median: ", "{:.2f}".format(statistics.median(arr)))
    print("Variance: ", "{:.2f}".format(statistics.pvariance(arr)))
    print("Range: ", "{:.2f}".format(max(arr) - min(arr)))