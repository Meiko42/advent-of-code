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

counter = 0
last = 0

group = 1
groupDict = {}
groupDict[group] = {}
groupMember = 1

while counter <= lastNum:
    if (counter == 0) or (counter in inputList):
        diff = counter - last
        if counter != 0:
            joltDiffDict[diff] += 1
        last = counter
        if diff == 3:
            group += 1
            groupDict[group] = {}
            groupMember = 1
        if groupMember <= 2:
            groupDict[group][counter] = 1
        if groupMember == 3:
            groupDict[group][counter] = 2
        if groupMember > 3:
            groupDict[group][counter] = 3
        groupMember += 1
    counter += 1

# Add another to 3 diff since that's always distance to your device adapter
joltDiffDict[3] += 1

# Charger value
charger = lastNum + 3

# Part 1 - Long Test Answer 220
# Part 1 - Answer 1890
part1Answer = joltDiffDict[1] * joltDiffDict[3]
print(part1Answer)

groupsToMult = []

for group, groupContent in groupDict.items():
    groupValuesList = []
    highest = 0
    removed = False
    for place, value in groupContent.items():
        groupValuesList.append(value)
    dropLast = (len(groupValuesList) - 1)
    groupValuesList[dropLast] = 0
    groupTotal = 0 
    for i in groupValuesList:
        groupTotal += i
    groupsToMult.append(groupTotal)
    

part2Answer = 1

for i in groupsToMult:
    if i != 0:
        part2Answer = part2Answer * i

# Part 2 - Answer is 49607173328384
print(part2Answer)