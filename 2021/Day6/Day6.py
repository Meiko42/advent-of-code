
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
    # input_file = "input.txt"
    input_file = "input-test.txt"
    inputs = read_input(input_file)

    inputs = inputs[0].split(',')

    allFish = []

    for fish in inputs:
        allFish.append(Angler(age=int(fish)))

    # for i in allFish:
    #     print(i.cycleTimer)


    experimentLength = 80

    for i in range(experimentLength):
        allFish = pass_one_day(allFish)


    print(len(allFish))

if __name__ == "__main__":
    main()