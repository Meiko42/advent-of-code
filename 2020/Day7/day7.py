# For a while I tried to deny that I needed a recursive function... 
# First time ever writing a recursive function on my own, so it's a mess. Will come back to it. 

import re
import pprint
from time import sleep

def RecursiveBagSearch(bagToSearchDict, checkedBags, bagsThatCanDict, bagToSearchNextDict):
    # print("!!!!!!!!!!!!!!!CALLED!!!!!!!!!!!!!!!")
    # print("bagToSearchDict")
    # pprint.pprint(bagToSearchDict)
    # print("checkedBags")
    # pprint.pprint(checkedBags)
    # print("bagsThatCanDict")
    # pprint.pprint(bagsThatCanDict)
    # print("bagToSearchNextDict")
    # pprint.pprint(bagToSearchNextDict)
    # sleep(10)
    for bag, value in bagToSearchDict.items():
        if bag not in checkedBags.keys():
            for bagType, bagContains in bagTypeInfoDict.items():
                if bag in bagContains.keys():
                    bagsThatCanDict[bagType] = True
                    bagToSearchNextDict[bagType] = True
        checkedBags[bag] = True
    bagToSearchDict = {}
    # pprint.pprint(bagToSearchNextDict)
    for bag, value in bagToSearchNextDict.items():
        if bag not in checkedBags.keys():
            bagToSearchDict[bag] = True
    # pprint.pprint(bagsThatCanDict)
    if len(bagToSearchDict.keys()) > 0:
        RecursiveBagSearch(bagToSearchDict, checkedBags, bagsThatCanDict, bagToSearchNextDict)
    else:
        return bagsThatCanDict

def RecursiveContentsSearch(bagToSearchDict, bagsContentsDict, bagToSearchNextDict):
    for bagSearch, contains in bagToSearchDict.items():
        if contains != "upperBagAmount":
            for bag, value in bagTypeInfoDict[bagSearch].items():
                    contains[bag] = {}
                    contains[bag]["upperBagAmount"] = value
                    RecursiveContentsSearch(contains[bag], bagsContentsDict, bagToSearchNextDict)



inputLineMatch = re.compile('^(\S+ \S+ bag)s contain (no other bags.|((\d+) (\S+ \S+ \S+(\, |\.)))+)')
# bagCanContainMatch = re.compile('^ ?(\d+) (\S+ \S+ \S+)((?<=(\.|\,))|((?<=(s\.|s\,))))')
bagCanContainMatch = re.compile('^ ?(\d+) (\S+ \S+ bag)')

with open('input.txt') as inputFile:
    inputVar = inputFile.readlines()

bagTypeInfoDict = {}

for line in inputVar:
    line = inputLineMatch.match(line)
    bagTypeInfoDict[line.group(1)] = {}
    if line.group(2) == "no other bags.":
        bagTypeInfoDict[line.group(1)]['isEmpty'] = True
    else:
        # print(line.group(2))
        bagCanContainLines = line.group(2)
        # This was originally:
        # bagCanContainLines = bagCanContainLines.split(',|.')
        # I shouldn't be allowed to do things.
        bagCanContainLines = bagCanContainLines.split(',')
        for entry in bagCanContainLines:
            entry = bagCanContainMatch.match(entry)
            bagTypeInfoDict[line.group(1)][entry.group(2)] = entry.group(1)

bagsThatCanDict = {}
bagsThatCanList = []

bagToSearchDict = {"shiny gold bag": True}
checkedBags = {}
bagToSearchNextDict = {}

RecursiveBagSearch(bagToSearchDict, checkedBags, bagsThatCanDict, bagToSearchNextDict)

# Part 1 - 177
print(len(bagsThatCanDict.keys()))

bagToSearchDict = {"shiny gold bag": {"upperBagAmount": 1}}
bagToSearchNextDict = {}
bagsContentsDict = {}
RecursiveContentsSearch(bagToSearchDict, bagsContentsDict, bagToSearchNextDict)

# print(len(bagsThatCanDict.keys()))





# for bagType, bagValues in bagTypeInfoDict.items():
#     if "isEmpty" not in bagValues.keys():
#         if "shiny gold bag" in bagValues.keys():
#             bagsThatCanDict[bagType] = True

# pprint.pprint(bagsThatCanDict)

# for bagType, bagValues in bagTypeInfoDict.items():
#     for bag in bagsThatCanDict.keys():
#         if (bag in bagValues.keys()) and (bag is not bagType):
#             bagsThatCanList.append(bag)

# pprint.pprint(bagsThatCanList)

# for i in bagsThatCanList:
#     bagsThatCanDict[bagType] = True

# answer = 0

# for i in bagsThatCanDict.keys():
#     answer += 1

# print(answer)

# pprint.pprint(bagsThatCanDict)


