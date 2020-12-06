import pprint
import re

validLineMatch = re.compile('^([a-z]+)')

sumOfAnswers = 0
seenInAnswerGroup = {}
with open('Input.txt') as inputFile:
    for line in inputFile:
        if line != "\n":
            lineMatch = validLineMatch.match(line)
            for item in lineMatch.group(1):
                seenInAnswerGroup[item] = True
        else:
            pprint.pprint(seenInAnswerGroup)
            sumOfAnswers =  sumOfAnswers + (len(seenInAnswerGroup.keys()))
            print(len(seenInAnswerGroup.keys()))
            seenInAnswerGroup = {}

sumOfAnswers =  sumOfAnswers + (len(seenInAnswerGroup.keys()))
            
print(sumOfAnswers)