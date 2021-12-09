def read_input(input_file):
    inputs = [x.strip().split('|') for x in open(input_file)]

    return inputs

# Playing with the numbers for the fuel consumption, found the sequence is triange numbers
# This makes the part 2 solution very easy


def main():
    input_file = "input.txt"
    # input_file = "input-test.txt"
    inputs = read_input(input_file)


    numSegmentsDict = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8]
    }

    part1Counter = 0

    for note in inputs:
        easyMatcher = []
        noteInput = note[0].split()
        converter = 
        # for i in noteInput:
        #     if len(i) in (2, 3, 4, 7):
        #         print(i)
        #         easyMatcher.append(i)
        noteOutput = note[1].split()
        for i in noteOutput:
            if len(i) in (2, 3, 4, 7):
                part1Counter += 1


    print(part1Counter)

    # numSegmentsDict = {
    #     0: 6, 
    #     1: 2,
    #     2: 5,
    #     3: 5, 
    #     4: 4,
    #     5: 5,
    #     6: 6,
    #     7: 3,
    #     8: 7,
    #     9: 6
    #     }





if __name__ == "__main__":
    main()