
def part1():
    counter = 0
    last = 0
    with open('input.txt') as input_file:
        for line in input_file:
            if (int(line) > last) and (last != 0):
                counter += 1
            last = int(line)

    print(counter)


counter1 = 0
counter2 = 0
last_measurement = 0
counter = 0

with open('input.txt') as input_file:
    for line in input_file:
        failed = False
        measurement = int(line) + counter1 + counter2
        if 0 in (counter1, counter2):
            failed = True
        if measurement > last_measurement and not failed and last_measurement != 0:
            counter += 1
        if not failed:
            last_measurement = measurement
        counter1 = counter2
        counter2 = int(line)

print(counter)
