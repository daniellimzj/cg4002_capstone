with open("daniel_grenade_2mins.csv", "r") as file:
    arr = []

    for line in file:
        arr.append(line.strip().split(","))

    print("total readings:", len(arr))

    i = 0
    count = 0
    while i < len(arr):
        while i < len(arr) and int(arr[i][1]) < -12000:
            i += 1

        i += 44
        count += 1

    print("windows counted:",count)