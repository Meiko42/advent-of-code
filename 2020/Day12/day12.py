
inputList = []

# West -=, East +=
x = 0
# South -=, North +=
y = 0  

compasReferenceDict = {0: "N", 1: "E", 2: "S", 3: "W"}

shipDirection = 1

with open("Input.txt") as inputFile:
    for line in inputFile:
        inputList.append(line.strip())


for instruction in inputList:
    print(instruction)
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
        print(f"Ship Direction Changed to: {shipDirection}")
    elif instruction[0] == "R":
        instruction = int(instruction.strip("R"))
        compasChange = instruction / 90
        shipDirection = shipDirection + compasChange
        if shipDirection > 3:
            shipDirection = shipDirection % 4
        print(f"Ship Direction Changed to: {shipDirection}")
    elif instruction[0] == "F":
        instruction = int(instruction.strip("F"))
        print(f"Moving {instruction} spaces in {shipDirection} direction")
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

part1Answer = abs(x) + abs(y)

# Part 1 - Answer 820
print(part1Answer)