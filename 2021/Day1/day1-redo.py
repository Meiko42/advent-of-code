
def read_input(input_file):
    inputs = [int(x) for x in open(input_file)]

    return inputs

def part1(inputs):
    counter = 0
    last = 0

    for value in inputs:
        if (value > last) and (last != 0):
            counter += 1
        last = value

    print(counter)

def part2(inputs):
    counter1 = 0
    counter2 = 0
    last_measurement = 0
    counter = 0

    for value in inputs:
        failed = False
        measurement = value + counter1 + counter2
        if 0 in (counter1, counter2):
            failed = True
        if measurement > last_measurement and not failed and last_measurement != 0:
            counter += 1
        if not failed:
            last_measurement = measurement
        counter1 = counter2
        counter2 = value

    print(counter)

def main():
    input_file = "input.txt"
    inputs = read_input(input_file)
    part1(inputs)
    part2(inputs)

if __name__ == "__main__":
    main()