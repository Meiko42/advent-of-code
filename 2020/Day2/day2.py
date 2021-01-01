import re

inputParse = re.compile('''^(\d+)-(\d+) (\S): (.+)''')

goodPassCount = 0
goodPassCount2 = 0

with open('Input.txt') as inputFile:
    for line in inputFile:
        parsedLine = inputParse.match(line)
        # print(parsedLine.group(4))
        # Groups: 1-lowest, 2-highest, 3-character, 4-password
        charCounter = 0
        charCounter2 = 0
        # Part 1
        for character in parsedLine.group(4):
            if character is parsedLine.group(3):
                charCounter += 1
        if charCounter >= int(parsedLine.group(1)) and charCounter <= int(parsedLine.group(2)):
            goodPassCount += 1
        # Part 2
        position1 = int(parsedLine.group(1)) - 1
        position2 = int(parsedLine.group(2)) - 1
        if parsedLine.group(4)[position1] is parsedLine.group(3):
            charCounter2 += 1
        if parsedLine.group(4)[position2] is parsedLine.group(3):
            charCounter2 += 1
        if charCounter2 == 1:
            goodPassCount2 += 1

# Answer: 614
print(goodPassCount)
# Answer: 354
print(goodPassCount2)