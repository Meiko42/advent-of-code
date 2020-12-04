import re

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID) - Missing this is fine for Part 1 and 2

day1Requirements = {'byr': True, 'iyr': True, 'eyr': True, 'hgt': True, 'hcl': True, 'ecl': True, 'pid': True, 'cid': False}

# For getting raw inputs into the passsportDict
initialImportMatch = re.compile('(\S+):(\S+)')

# For part 2 we start to validate the fields, except for 'cid'
byrValidMatch = re.compile('^19[2-9][0-9]|200[0-2]$')
iyrValidMatch = re.compile('^201[0-9]|2020$')
eyrValidMatch = re.compile('^202[0-9]|2030$')
hgtValidMatch = re.compile('^((15[0-9]|16[0-9]|17[0-9]|18[0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in)$')
hclValidMatch = re.compile('^#[a-f0-9]{6}$')
eclValidMatch = re.compile('^amb|blu|brn|gry|grn|hzl|oth$')
pidValidMatch = re.compile('^[0-9]{9}$')

passportsDict = {}
passportsCount = 1
passportsDict[passportsCount] = {}

with open('Input.txt') as inputFile:
    for line in inputFile:
        if line != "\n":
            inputPrep = line.split()
            for item in inputPrep:
                itemReg = initialImportMatch.match(item)
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
    InvalidPassportFlag = 0
    if ('validityPart1' in passportEntries.keys()) and (passportEntries['validityPart1'] == False):
        numberOfInvalidPassportsP1 += 1
        InvalidPassportFlag = 1
    else:
        # From here on we know all passport entries that are required will be present in the dict.
        # byr
        if not byrValidMatch.match(passportEntries['byr']):
            InvalidPassportFlag = 1
        # iyr
        if not iyrValidMatch.match(passportEntries['iyr']):
            InvalidPassportFlag = 1
        # eyr
        if not eyrValidMatch.match(passportEntries['eyr']):
            InvalidPassportFlag = 1
        # hgt
        if not hgtValidMatch.match(passportEntries['hgt']):
            InvalidPassportFlag = 1
        # hcl
        if not hclValidMatch.match(passportEntries['hcl']):
            InvalidPassportFlag = 1
        # ecl
        if not eclValidMatch.match(passportEntries['ecl']):
            InvalidPassportFlag = 1
        # pid
        if not pidValidMatch.match(passportEntries['pid']):
            InvalidPassportFlag = 1
    numberOfInvalidPassportsP2 += InvalidPassportFlag

totalPassports = len(passportsDict)

# Part 1 - Answer is 206
print(totalPassports - numberOfInvalidPassportsP1)
# Part 2 - Answer is 123
print(totalPassports - numberOfInvalidPassportsP2)