import os

start = 33
end = 43

action = "logout"

for i in range(start,end):

    os.rename("p1_wrist" + f'{i:04}' + ".txt", "p1_" + action + f'{(i - start + 1):04}' + ".txt")
    os.rename("p2_wrist" + f'{i:04}' + ".txt", "p2_" + action + f'{(i - start + 1):04}' + ".txt")