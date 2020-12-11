# The test input from part 1 is the longer one, not the intial short one. 

inputList = []

endsList = [2147483647, 0]

joltDiffDict = {1: 0, 2: 0, 3: 0}

with open("Input.txt") as inputFile:
    for line in inputFile:
        line = int(line.split()[0])
        inputList.append(line)
        if line < endsList[0]:
            endsList[0] = line
        if line > endsList[1]:
            endsList[1] = line

firstNum = endsList[0]
lastNum = endsList[1]

counter = firstNum
last = 0

while counter <= lastNum:
    if counter in inputList:
        diff = counter - last
        joltDiffDict[diff] += 1
        last = counter
    counter += 1

# Add another to 3 diff since that's always distance to your device adapter
joltDiffDict[3] += 1

# Part 1 - Answer 1890
part1Answer = joltDiffDict[1] * joltDiffDict[3]
print(part1Answer)