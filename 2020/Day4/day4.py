# This code makes me sad. I'm going to redo when I have a good chunk of time to focus

import re

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID) - Missing this is fine for Part 1

def ValueChecker(*args, **kwargs):
    pass

day1Requirements = {'byr': True, 'iyr': True, 'eyr': True, 'hgt': True, 'hcl': True, 'ecl': True, 'pid': True, 'cid': False}

# For Part 1 we accept fields that are present without validating their values
lolMatch = re.compile('(\S+):(\S+)')

# For part 2 we start to validate the fields 
hgtValidMatch = re.compile('((15[0-9]|16[0-9]|17[0-9]|18[0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in)')
hclValidMatch = re.compile('^#[a-f0-9]{6}')
eclValidMatch = re.compile('^(amb|blu|brn|gry|grn|hzl|oth)$')
pidValidMatch = re.compile('^([0-9]{9})$')




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

numberOfInvalidPassportsP1 = 0
numberOfInvalidPassportsP2 = 0

for passport, passportEntries in passportsDict.items():
    for requirement in day1Requirements.keys():
        if (requirement not in passportEntries.keys()) and (day1Requirements[requirement] is True):
            passportsDict[passport]['validityPart1'] = False
        
for passport, passportEntries in passportsDict.items():
    if ('validityPart1' in passportEntries.keys()) and (passportEntries['validityPart1'] == False):
        numberOfInvalidPassportsP1 += 1
        passportEntries['validityPart2'] = False
    else:
        # At this point we know the entries will have all required fields
        # byr
        if (int(passportEntries['byr']) < 1920) or (int(passportEntries['byr']) > 2002):
            passportEntries['validityPart2'] = False
        # iyr
        if (int(passportEntries['iyr']) < 2010) or (int(passportEntries['iyr']) > 2020):
            passportEntries['validityPart2'] = False
        # eyr
        if (int(passportEntries['eyr']) < 2020) or (int(passportEntries['eyr']) > 2030):
            passportEntries['validityPart2'] = False
        # hgt
        if not hgtValidMatch.match(passportEntries['hgt']):
            passportEntries['validityPart2'] = False
        # hcl
        if not hclValidMatch.match(passportEntries['hcl']):
            passportEntries['validityPart2'] = False
        # ecl
        if not eclValidMatch.match(passportEntries['ecl']):
            passportEntries['validityPart2'] = False
        # pid
        if not pidValidMatch.match(passportEntries['pid']):
            passportEntries['validityPart2'] = False
            print("wow")

for passport, passportEntries in passportsDict.items():
    if ('validityPart2' in passportEntries.keys()) and (passportEntries['validityPart2'] == False):
        numberOfInvalidPassportsP2 += 1

totalPassports = len(passportsDict)

# Part 1 - Answer is 206
print(totalPassports - numberOfInvalidPassportsP1)
# Part 2 - Answer is 123
print(totalPassports - numberOfInvalidPassportsP2)