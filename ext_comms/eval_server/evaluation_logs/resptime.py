import json
import statistics

id = int(input("eval run id: "))

with open("groupb11_logs.json", "r") as file:

    arr = []

    for line in file:
        reading = json.loads(line)

        if reading['id'] == id:
            arr.append(reading['response_time'])

    print(statistics.median(arr), statistics.mean(arr), min(arr), max(arr))
