
inputList = []

# West -=, East +=
# x = 0
# South -=, North +=
# y = 0  

compasReferenceDict = {0: "N", 1: "E", 2: "S", 3: "W"}

# shipDirection = 1

with open("Input.txt") as inputFile:
    for line in inputFile:
        inputList.append(line.strip())

def part1Navigation(inputList):
    # West -=, East +=
    x = 0
    # South -=, North +=
    y = 0

    shipDirection = 1

    for instruction in inputList:
        if instruction[0] == "N":
            instruction = int(instruction.strip("N"))
            y += instruction
        elif instruction[0] == "S":
            instruction = int(instruction.strip("S"))
            y -= instruction
        elif instruction[0] == "E":
            instruction = int(instruction.strip("E"))
            x += instruction
        elif instruction[0] == "W":
            instruction = int(instruction.strip("W"))
            x -= instruction
        elif instruction[0] == "L":
            instruction = int(instruction.strip("L"))
            compasChange = instruction / -90
            shipDirection = shipDirection + compasChange + 4
            if shipDirection > 3:
                shipDirection = shipDirection % 4
        elif instruction[0] == "R":
            instruction = int(instruction.strip("R"))
            compasChange = instruction / 90
            shipDirection = shipDirection + compasChange
            if shipDirection > 3:
                shipDirection = shipDirection % 4
        elif instruction[0] == "F":
            instruction = int(instruction.strip("F"))
            if shipDirection == 0:
                y += instruction
            if shipDirection == 2:
                y -= instruction
            if shipDirection == 1:
                x += instruction
            if shipDirection == 3:
                x -= instruction
        else:
            print("You shouldn't be here")
            quit()

    return x, y

def part2WaypointAdjust(y, x, adjustments):

    xTemp = x
    yTemp = y

    while adjustments > 0:
        xNew = 0 - yTemp
        yNew = xTemp
        adjustments -= 1
        xTemp = xNew
        yTemp = yNew

    return xNew, yNew


def part2Navigation(inputList):
    # West -=, East +=
    x = 10
    # South -=, North +=
    y = 1

    shipX = 0 
    shipY= 0 

    for instruction in inputList:
        if instruction[0] == "N":
            instruction = int(instruction.strip("N"))
            y += instruction
        elif instruction[0] == "S":
            instruction = int(instruction.strip("S"))
            y -= instruction
        elif instruction[0] == "E":
            instruction = int(instruction.strip("E"))
            x += instruction
        elif instruction[0] == "W":
            instruction = int(instruction.strip("W"))
            x -= instruction
        elif instruction[0] == "L":
            instruction = int(instruction.strip("L"))
            compasChange = instruction // 90
            if compasChange == 1:
                compasChange = 3
                y, x = part2WaypointAdjust(x, y, compasChange)
            elif compasChange == 2:
                y, x = part2WaypointAdjust(x, y, compasChange)
            elif compasChange == 3:
                compasChange = 1
                y, x = part2WaypointAdjust(x, y, compasChange)
            else: 
                print("YOU SHOULDNT BE HERE. L Change went wrong")
                quit()
        elif instruction[0] == "R":
            instruction = int(instruction.strip("R"))
            compasChange = instruction // 90
            y, x = part2WaypointAdjust(x, y, compasChange)
        elif instruction[0] == "F":
            instruction = int(instruction.strip("F"))
            while instruction > 0:
                shipX = shipX + x
                shipY = shipY + y
                instruction -= 1
        else:
            print("You shouldn't be here")
            quit()

    return shipX, shipY

part1x, part1y = part1Navigation(inputList)
part2x, part2y = part2Navigation(inputList)

part1Answer = abs(part1x) + abs(part1y)
part2Answer = abs(part2x) + abs(part2y)

# Part 1 - Answer 820
print(part1Answer)

# Part 2 - Answer 66614
print(part2Answer)

