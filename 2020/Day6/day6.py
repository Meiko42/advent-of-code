import pprint
import re

validLineMatch = re.compile('^([a-z]+)')

# Part 2
# For a given group, need number of questions every person in the group put "yes" to
# Then at the end add all of them up. 


# Part 1 total
sumOfAnswers = 0
# Part 1 - Tracks all questions seen in a single group 
seenInAnswerGroup = {}

# Part 2 - All answers for a group and how many times it was answered
numAnswersInGroup = {}

# Part 2 - Number of people in a groups
numPeopleInGroup = 0

# Part 2 - Num of questions all people had
numGroupTotal = 0

# Part 2 - Total list
numAnswersList = []

with open('Input.txt') as inputFile:
    for line in inputFile:
        if line != "\n":
            numPeopleInGroup += 1
            lineMatch = validLineMatch.match(line)
            for item in lineMatch.group(1):
                seenInAnswerGroup[item] = True
                if item not in numAnswersInGroup.keys():
                    numAnswersInGroup[item] = 1
                else:
                    numAnswersInGroup[item] += 1
        else:
            # pprint.pprint(seenInAnswerGroup)
            sumOfAnswers =  sumOfAnswers + (len(seenInAnswerGroup.keys()))
            for key, value in numAnswersInGroup.items():
                if value == numPeopleInGroup:
                    numGroupTotal += 1
            numAnswersList.append(numGroupTotal)
            # print(len(seenInAnswerGroup.keys()))
            seenInAnswerGroup = {}
            numAnswersInGroup = {}
            numPeopleInGroup = 0
            numGroupTotal = 0

for key, value in numAnswersInGroup.items():
    if value == numPeopleInGroup:
        numGroupTotal += 1
numAnswersList.append(numGroupTotal)
sumOfAnswers =  sumOfAnswers + (len(seenInAnswerGroup.keys()))

# Part 1 - 6748
print(sumOfAnswers)

# Part 2 - 3445
part2Answer = 0
for i in numAnswersList:
    part2Answer += i

print(part2Answer)