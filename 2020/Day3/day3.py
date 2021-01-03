import re 

with open('Input.txt') as inputFile:
    inputList = inputFile.readlines()

with open('part2Input.txt') as InputFile2:
    inputList2 = InputFile2.readlines()


inputList2Parse = re.compile('''^Right (\d), down (\d)''')




# We're going to assume each line is the same length
lineLength = len(inputList[0].strip())

# Starting with the first line in the upper left corner:
# 1 - Capture the current position of the "pointer", if "#" increment treesCount
# 2 - Increment the pointer by 3
# 3 - If pointer is more than lineLength, set "pointer" to lineLength modulo pointer
# 4 - Move on to the next line



def slopeCheck(overNum, downNum):
    treesCounter = 0
    pointer = 0
    downCounter = 0
    for line in inputList:
        modVal = downCounter % downNum
        if (modVal == 0):
            line = line.strip()
            if line[pointer] == "#":
                treesCounter = treesCounter + 1
            pointer = pointer + overNum
            if pointer >= lineLength:
                pointer = pointer % lineLength
        downCounter += 1
    return treesCounter

# Part 1 Answer: 268
print("Part 1:")
print(slopeCheck(3, 1))

# Part 2
print("\nPart 2:")
part2ValuesList = []
for line in inputList2:
    parsedLine = inputList2Parse.match(line)
    part2ValuesList.append(slopeCheck(int(parsedLine[1]), int(parsedLine[2])))

print(part2ValuesList)

part2Answer = 1

for entry in part2ValuesList:
    part2Answer = part2Answer * entry
print(part2Answer)