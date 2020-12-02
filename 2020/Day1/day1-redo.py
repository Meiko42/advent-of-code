def partOne(inputDict):
    for key, value in inputDict.items():
        if value in inputDict.keys():
            print(f"Part 1: Found {key}, {value}")
            answer = key * value
            print(f"Part 1: Answer is {answer}")
            return

def partTwo(inputDict):
    for value1 in inputDict.values():
        for value2 in inputDict.values():
            complement = value1 + value2
            if complement in inputDict.keys():
                value3 = inputDict.get(complement)
                print(f"Part 2: Found {value1}, {value2}, {value3}")
                answer = value1 * value2 * value3
                print(f"Part 2: Answer is {answer}")
                return

def main():

    inputDict = {}
    inputDictFlip = {}

    with open("Input.txt") as inputFile:
        for line in inputFile:
            complement = 2020 - int(line)
            inputDict[int(line.rstrip())] = complement
            inputDictFlip[complement] = int(line.rstrip())

    partOne(inputDict)

    partTwo(inputDictFlip)


if __name__ == "__main__":
    main()