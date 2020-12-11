import copy

inputDict = {}
instructionCounter = 1

with open("Input.txt") as inputFile:
    for line in inputFile:
        line = line.split()
        inputDict[instructionCounter] = {}
        inputDict[instructionCounter]["instruction"] = line[0]
        inputDict[instructionCounter]["value"] = int(line[1])
        inputDict[instructionCounter]["executed"] = False
        instructionCounter += 1

def runProgram(inputDict, instructionCounter):
    accumulator = 0
    lastInstruction = False
    while True:
        if instructionCounter == (len(inputDict.keys()) - 1):
            lastInstruction = True
        if inputDict[instructionCounter]["executed"] is False:
            inputDict[instructionCounter]["executed"] = True
            if inputDict[instructionCounter]["instruction"] == "acc":
                accumulator = accumulator + int(inputDict[instructionCounter]["value"])
                instructionCounter += 1
                if lastInstruction is True:
                    return accumulator, True
            if inputDict[instructionCounter]["instruction"] == "jmp":
                instructionCounter += inputDict[instructionCounter]["value"]
                if lastInstruction is True:
                    return accumulator, True
            if inputDict[instructionCounter]["instruction"] == "nop":
                instructionCounter += 1
                if lastInstruction is True:
                    return accumulator, True
        else:
            # Part 1 - Answer is 1200
            return accumulator, False

def patchProgram(inputDict):
    instCount = 1
    while True:
        checked = False
        modifiedProgramDict = copy.deepcopy(inputDict)
        if instCount > len(inputDict.keys()):
            return "Failed", False
        if modifiedProgramDict[instCount]["instruction"] == "jmp":
            modifiedProgramDict[instCount]["instruction"] = "nop"
            accumulator, terminated = runProgram(modifiedProgramDict, int(1))
            if terminated is True: 
                return accumulator, True
            else:
                checked = True
        if (modifiedProgramDict[instCount]["instruction"] == "nop") and (checked is False):
            modifiedProgramDict[instCount]["instruction"] = "jmp"
            accumulator, terminated = runProgram(modifiedProgramDict, int(1))
            if terminated is True: 
                return accumulator, True
        instCount += 1

inputDictP1 = copy.deepcopy(inputDict)

# Part 1 - Answer 1200
answer1 = runProgram(inputDictP1, int(1))[0]
print(answer1)

# Part 2 - Answer 1023
answer2 = patchProgram(inputDict)[0]
print(answer2)