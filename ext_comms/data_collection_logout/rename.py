import os
for i in range(1,41):

    os.rename("p2_wrist_" + f'{i:04}' + ".txt", "p2_logout" + f'{i:04}' + ".txt")
