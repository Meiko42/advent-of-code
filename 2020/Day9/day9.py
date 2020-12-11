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
                # print("CYCLE")
                # print(inputList[pointer1])
                # print(inputList[pointer2])
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

print(firstInvalid(inputList, 25))