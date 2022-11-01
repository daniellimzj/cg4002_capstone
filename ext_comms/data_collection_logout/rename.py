import os
for i in range(41,43):

    os.rename("p1_wrist_" + f'{i:04}' + ".txt", "p1_logout" + f'{i:04}' + ".txt")
