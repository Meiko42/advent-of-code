import re
import pprint

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID) - Missing this is fine for Part 1

day1Requirements = {'byr': True, 'iyr': True, 'eyr': True, 'hgt': True, 'hcl': True, 'ecl': True, 'pid': True, 'cid': False}

lolMatch = re.compile('(\S+):(\S+)')

passportsDict = {}
passportsCount = 1
passportsDict[passportsCount] = {}

with open('Input.txt') as inputFile:
    for line in inputFile:
        if line != "\n":
            inputPrep = line.split()
            for item in inputPrep:
                itemReg = lolMatch.match(item)
                passportsDict[passportsCount][itemReg.group(1)] = itemReg.group(2)
        else:
            passportsCount += 1
            passportsDict[passportsCount] = {}

numberOfInvalidPassports = 0

for passport, passportEntries in passportsDict.items():
    for requirement in day1Requirements.keys():
        if (requirement not in passportEntries.keys()) and (day1Requirements[requirement] is True):
            passportsDict[passport]['validityPart1'] = False
        
for passport, passportEntries in passportsDict.items():
    if ('validityPart1' in passportEntries.keys()) and (passportEntries['validityPart1'] == False):
        numberOfInvalidPassports += 1

totalPassports = len(passportsDict)

print(totalPassports - numberOfInvalidPassports)