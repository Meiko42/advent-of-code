def partOne(inputDict):
    for key, value in inputDict.items():
        if value in inputDict.keys():
            print(f"Part 1: Found {key}, {value}")
            answer = key * value
            print(f"Part 1: Answer is {answer}")
            return

def partTwo(inputDict):
    for key1 in inputDict.keys():
        for key2 in inputDict.keys():
            for key3 in inputDict.keys():
                if key1 + key2 + key3 == 2020:
                    print(f"Part 2: Found {key1}, {key2}, {key3}")
                    answer = key1 * key2 * key3
                    print(f"Part 2: Answer is {answer}")
                    return

def main():

    inputDict = {}

    with open("Input.txt") as inputFile:
        for line in inputFile:
            complement = 2020 - int(line)
            inputDict[int(line.rstrip())] = complement

    # Answer: 
    # Part 1: Found 1477, 543
    # Part 1: Answer is 802011
    partOne(inputDict)

    partTwo(inputDict)


if __name__ == "__main__":
    main()