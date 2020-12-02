import re

inputParse = re.compile('''^(\d+)-(\d+) (\S): (.+)''')

goodPassCount = 0

with open('Input.txt') as inputFile:
    for line in inputFile:
        parsedLine = inputParse.match(line)
        # print(parsedLine.group(4))
        # Groups: 1-lowest, 2-highest, 3-character, 4-password
        charCounter = 0
        for character in parsedLine.group(4):
            if character is parsedLine.group(3):
                charCounter += 1
        if charCounter >= int(parsedLine.group(1)) and charCounter <= int(parsedLine.group(2)):
            goodPassCount += 1

print(goodPassCount)