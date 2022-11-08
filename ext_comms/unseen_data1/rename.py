import os

start = 32
end = 42

for i in range(start,end):

    os.rename("p1_wrist" + f'{i:04}' + ".txt", "p1_logout" + f'{(i - start + 1):04}' + ".txt")
    os.rename("p2_wrist" + f'{i:04}' + ".txt", "p2_logout" + f'{(i - start + 1):04}' + ".txt")