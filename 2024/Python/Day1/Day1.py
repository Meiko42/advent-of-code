#!/usr/bin/env python3

leftList = []
rightList = []

with open("input", "r") as inputFile:
    for line in inputFile:
        left, right = map(int, line.split())
        leftList.append(left)
        rightList.append(right)

leftList.sort()
rightList.sort()

part1 = 0

for position, leftValue in enumerate(leftList):
    distance = abs(leftValue - rightList[position])
    part1 += distance

print(f"Part one answer: {part1}")
