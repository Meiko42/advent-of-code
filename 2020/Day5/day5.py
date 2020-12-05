import re

inputRawMatch = re.compile('^([B|F]{7})([R|L]{3})')

passesDict = {}
passesCount = 1

with open('Input.txt') as inputFile:
    for line in inputFile:
        inputMatched = inputRawMatch.match(line)
        passesDict[passesCount] = {}
        passesDict[passesCount]['rowInput'] = inputMatched.group(1)
        passesDict[passesCount]['columnInput'] = inputMatched.group(2)
        passesCount += 1

seenBoardingPassNums = {}

for key, value in passesDict.items():
    replaceString = str(value['rowInput'])
    replaceString = replaceString.replace('B', '1')
    replaceString = replaceString.replace('F', '0')
    value['rowInput'] = int(replaceString, base=2)

    replaceString = str(value['columnInput'])
    replaceString = replaceString.replace('R', '1')
    replaceString = replaceString.replace('L', '0')
    value['columnInput'] = int(replaceString, base=2)
    # For part 2
    seenBoardingPassNums[passesDict[key]['rowInput'] * 8 + passesDict[key]['columnInput']] = True

# pprint.pprint(passesDict)

bestSeenColumnDict = {'winner': {'rowInput': 0, 'columnInput': 0, 'passNumber': 0}}

for key, value in passesDict.items():
    if value['rowInput'] > bestSeenColumnDict['winner']['rowInput']:
        bestSeenColumnDict['winner']['rowInput'] = value['rowInput']
        bestSeenColumnDict['winner']['columnInput'] = value['columnInput']
        bestSeenColumnDict['winner']['passNumber'] = int(key)

winningRow = bestSeenColumnDict['winner']['rowInput']

bestSeenRowDict = {'winner': {'rowInput': 0, 'columnInput': 0, 'passNumber': 0}}

for key, value in passesDict.items():
    if (value['columnInput'] > bestSeenColumnDict['winner']['columnInput']) and (value['rowInput'] == winningRow):
        bestSeenRowDict['winner']['rowInput'] = value['rowInput']
        bestSeenRowDict['winner']['columnInput'] = value['columnInput']
        bestSeenRowDict['winner']['passNumber'] = int(key)

highestSeatId = bestSeenRowDict['winner']['rowInput'] * 8 + bestSeenRowDict['winner']['columnInput']

print(f"Part 1: {highestSeatId}")

for number in range(highestSeatId):
    number += 1
    if number not in seenBoardingPassNums.keys():
        aheadNum = number + 1
        behindNum = number - 1
        if (aheadNum in seenBoardingPassNums.keys()) and (behindNum in seenBoardingPassNums.keys()):
            print(f"Part 2: {number}")