#!/usr/bin/env python3

leftList = []
rightList = []

# {leftNum: {left_occurances: 1, right_occurances: 0}}
similarityDict = {}

with open("input", "r") as inputFile:
    for line in inputFile:
        left, right = map(int, line.split())

        leftList.append(left)

        if left in similarityDict.keys():
            similarityDict[left]["left_occurances"] += 1
        else:
            similarityDict[left] = {"left_occurances": 1, "right_occurances": 0}

        rightList.append(right)

        if right in similarityDict.keys():
            similarityDict[right]["right_occurances"] += 1
        else:
            similarityDict[right] = {"left_occurances": 0, "right_occurances": 1}


leftList.sort()
rightList.sort()

part1 = 0

for position, leftValue in enumerate(leftList):
    distance = abs(leftValue - rightList[position])
    part1 += distance

print(f"Part one answer: {part1}")

similarityScore = 0

for locationID, locationIDComparison in similarityDict.items():
    similarityScore += locationID * locationIDComparison["right_occurances"] * locationIDComparison["left_occurances"]

print(f"Part two answer: {similarityScore}")
