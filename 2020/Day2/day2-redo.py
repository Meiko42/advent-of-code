import re

# Groups: 1 - lowest/position1, 2 - highest/position2, 3 - character, 4 - password
inputParse = re.compile('''^(\d+)-(\d+) (\S): (.+)''')

goodPassCount = 0
goodPassCount2 = 0

with open('Input.txt') as inputFile:
    inputList = inputFile.readlines()

for line in inputList:
    parsedLine = inputParse.match(line)
    charCounter = 0
    charCounter2 = 0

    # Part 1 - answer is 614
    charCounter = parsedLine.group(4).count(parsedLine.group(3))
    if charCounter >= int(parsedLine.group(1)) and charCounter <= int(parsedLine.group(2)):
        goodPassCount += 1

    # Part 2 - answer is 354
    position1 = int(parsedLine.group(1)) - 1
    position2 = int(parsedLine.group(2)) - 1
    if parsedLine.group(4)[position1] is parsedLine.group(3):
        charCounter2 += 1
    if parsedLine.group(4)[position2] is parsedLine.group(3):
        charCounter2 += 1
    if charCounter2 == 1:
        goodPassCount2 += 1

print(f"Part 1 Answer: {goodPassCount}")
print(f"Part 2 Answer: {goodPassCount2}")