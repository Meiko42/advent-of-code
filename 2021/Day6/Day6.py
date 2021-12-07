
class Angler:
    def __init__(self, age=None):
        if not age:
            self.cycleTimer = 8
        else:
            self.cycleTimer = int(age)
    
    def increaseAge(self, days):
        self.cycleTimer -= days

    def setAge(self, days):
        self.cycleTimer = days
    


def read_input(input_file):
    inputs = [x for x in open(input_file)]

    return inputs

def pass_one_day(allFish):

    newAnglers = []

    for existingAngler in allFish:
        # print(existingAngler.cycleTimer)
        if existingAngler.cycleTimer == 0:
            existingAngler.setAge(6)
            newAnglers.append(Angler(age=8))
        else:
            existingAngler.increaseAge(1)

    for new in newAnglers:
        allFish.append(new)

    return allFish


def main():
    input_file = "input.txt"
    # input_file = "input-test.txt"
    inputs = read_input(input_file)

    inputs = inputs[0].split(',')

    allFish = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }

    for fish in inputs:
        allFish[int(fish)] += 1

    # for i in allFish:
    #     print(i.cycleTimer)

    experimentLength = 256
    for i in range(experimentLength):
        resetExisting = allFish[0]
        newFishCounter = allFish[0]
        allFish[0] = allFish[1]
        allFish[1] = allFish[2]
        allFish[2] = allFish[3]
        allFish[3] = allFish[4]
        allFish[4] = allFish[5]
        allFish[5] = allFish[6]
        allFish[6] = allFish[7]
        allFish[6] += resetExisting
        allFish[7] = allFish[8]
        allFish[8] = newFishCounter
        print(allFish)

    totalFish = 0
    for key, value in allFish.items():
        totalFish += value

    print(totalFish)

if __name__ == "__main__":
    main()