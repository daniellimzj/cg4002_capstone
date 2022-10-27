import os

for i in range(1, 25):

    oldfile = "p2_wrist_" + f'{i:04}' + ".txt"

    action = ""

    if 0 < i and i < 7:
        action = "grenade"

    elif 6 < i and i < 13:
        action = "shield"

    elif 12 < i and i < 19:
        action = "reload"

    else:
        action = "logout"

    newname = "p2_" + action + f'{((i % 6) + 1):04}' + ".txt"

    os.rename(oldfile, newname)