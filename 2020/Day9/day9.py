with open("Input.txt") as inputFile:
    inputList = []
    for line in inputFile:
        inputList.append(int(line.strip()))

def firstInvalid(inputList, preamble):
    preamble = preamble - 1
    startingIndex = 0
    endingIndex = startingIndex + preamble
    pointer1 = startingIndex
    pointer2 = pointer1 + 1
    value = endingIndex + 1
    valid = False
    step = 0
    while value <= len(inputList):
        while pointer1 != endingIndex:
            while pointer2 <= endingIndex:
                if inputList[pointer1] + inputList[pointer2] == inputList[value]:
                    valid = True
                pointer2 += 1
            pointer1 += 1
            pointer2 = pointer1 + 1
        if not valid:
            return inputList[value]
        step += 1
        startingIndex = step
        endingIndex = startingIndex + preamble
        pointer1 = startingIndex
        pointer2 = pointer1 + 1
        value = endingIndex + 1
        valid = False

def scanSum(inputList, target):
    startingIndex = 0
    step = 0 
    total = 0
    # Low, High
    endsList = [2147483647, 0]
    while True:
        while total < target:
            value = inputList[step]
            total += value
            step += 1
            if value < endsList[0]:
                endsList[0] = value
            if value > endsList[1]:
                endsList[1] = value
            if total == target:
                return endsList[0] + endsList[1]
        startingIndex += 1
        step = startingIndex
        total = 0
        endsList = [2147483647, 0]

# Part 1 - Answer 69316178
part1Answer = firstInvalid(inputList, 25)
print(part1Answer)

# Part 2 - Answer 9351526
print(scanSum(inputList, part1Answer))
