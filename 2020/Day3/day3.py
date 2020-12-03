
with open('Input.txt') as inputFile:
    inputList = inputFile.readlines()

# We're going to assume each line is the same length
lineLength = len(inputList[0].strip())

# Starting with the first line in the upper left corner:
# 1 - Capture the current position of the "pointer", if "#" increment treesCount
# 2 - Increment the pointer by 3
# 3 - If pointer is more than lineLength, set "pointer" to lineLength modulo pointer
# 4 - Move on to the next line

treesCounter = 0
pointer = 0

for line in inputList:
    line = line.strip()
    print(line[pointer])
    if line[pointer] == "#":
        treesCounter = treesCounter + 1
    pointer = pointer + 3
    if pointer >= lineLength:
        pointer = pointer % lineLength

print(treesCounter)