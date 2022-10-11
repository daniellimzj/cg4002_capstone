with open("daniel_grenade_2mins.csv", "r") as file:
    arr = []

    for line in file:
        arr.append(line.strip().split(","))

    print(len(arr))
    print(arr[5])

    i = 0
    count = 0
    while i < len(arr):
        while i < len(arr) and int(arr[i][1]) < -12000:
            i += 1

        i += 43
        count += 1

    print(count)