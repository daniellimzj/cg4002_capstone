import numpy as np
import statistics


a = [100, 100, 12, 30, 40, 80, 120, 160, 250, 410, 12, 13]
a.sort()
print(a)

print(statistics.quantiles(a), np.percentile(a, 25), np.percentile(a, 75))