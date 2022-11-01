import json

with open("groupb11_logs.json", "r") as file:

    count = 0
    sum = 0

    for line in file:
        reading = json.loads(line)

        if reading['id'] == 3384:
            count += 1
            sum += reading['response_time']

    print(count, sum, sum / count)
