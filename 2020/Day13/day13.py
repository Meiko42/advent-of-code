import pprint

inputDict = {}

with open("Input.txt") as inputFile:
    for line in inputFile:
        if "," not in line:
            line = line.strip()
            inputDict[line] = {}
            inputDictSub = inputDict[line] 
        else:
            line = line.split(",")
            for entry in line:
                print(entry)
                inputDictSub[entry] = True


pprint.pprint(inputDict)

busArrivalDict = {}

worstList = [0, 0]

for timestamp, buses in inputDict.items():
    for bus, _ in buses.items():
        if bus != "x":
            busArrivalDict[int(bus)] = {}

            mult = int(timestamp) // int(bus)
            busArrivalTime = int(bus) * (mult + 1)

            busArrivalDict[int(bus)]["bestArrival"] = busArrivalTime
            busArrivalDict[int(bus)]["bestWaiting"] = busArrivalTime - int(timestamp)

            if busArrivalTime > worstList[1]:
                worstList[0] = int(bus)
                worstList[1] = busArrivalTime

bestList = worstList

for bus, values in busArrivalDict.items():
    if values["bestWaiting"] < bestList[1]:
        bestList[0] = int(bus)
        bestList[1] = values["bestWaiting"]

part1Answer = bestList[0] * bestList[1]

print(part1Answer)