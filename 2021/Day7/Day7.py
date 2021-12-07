def read_input(input_file):
    inputs = [x for x in open(input_file)]

    return inputs


def main():
    # input_file = "input.txt"
    input_file = "input-test.txt"
    inputs = read_input(input_file)

    positionsDict = {}

    inputs = inputs[0].split(',')

    largestPositionNumber = 0
    for i in inputs:
        if int(i) not in positionsDict:
            positionsDict[int(i)] = {}
            positionsDict[int(i)]["subsOnPosition"] = 0
        positionsDict[int(i)]["subsOnPosition"] += 1
        if int(i) > largestPositionNumber:
            largestPositionNumber = int(i)
    
    lowestFuel = None
    mostFuelEfficientLocation = 0
    for i in range(largestPositionNumber+1):
        fuelExpense = 0
        if i not in positionsDict:
            positionsDict[i] = {}
            positionsDict[i]["subsOnPosition"] = 0
        for position, values in positionsDict.items():
            if values["subsOnPosition"] != 0:
                # Part1
                fuelExpense += abs((position - i) * values["subsOnPosition"])
        positionsDict[i]["fuelExpense"] = fuelExpense
        if lowestFuel is None:
            lowestFuel = fuelExpense
            mostFuelEfficientLocation = i
        else:
            if fuelExpense < lowestFuel:
                lowestFuel = fuelExpense
                mostFuelEfficientLocation = i


    print(mostFuelEfficientLocation)
    print(lowestFuel)

    

    # mostOnSpot = 0
    # sumOccupiedPositionNumbers = 0
    # for key, value in positionsDict.items():
    #     sumOccupiedPositionNumbers += key
    #     if value > mostOnSpot:
    #         mostOnSpot = value
    #         winner = {key: value}





if __name__ == "__main__":
    main()