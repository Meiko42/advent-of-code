import pprint

inputDict = {}
instructionCounter = 1
 
with open("Input.txt") as inputFile:
    for line in inputFile:
        line = line.split()
        # print(line)
        inputDict[instructionCounter] = {}
        inputDict[instructionCounter]["instruction"] = line[0]
        inputDict[instructionCounter]["value"] = int(line[1])
        inputDict[instructionCounter]["executed"] = False
        instructionCounter += 1

instructionCounter = 1
accumulator = 0

pprint.pprint(inputDict)

while True:
    print(inputDict[instructionCounter]["executed"])
    if inputDict[instructionCounter]["executed"] is False:
        inputDict[instructionCounter]["executed"] = True
        if inputDict[instructionCounter]["instruction"] == "acc":
            accumulator = accumulator + int(inputDict[instructionCounter]["value"])
            instructionCounter += 1
        if inputDict[instructionCounter]["instruction"] == "jmp":
            instructionCounter += inputDict[instructionCounter]["value"]
        if inputDict[instructionCounter]["instruction"] == "nop":
            instructionCounter += 1
    else:
        print(accumulator)
        quit()