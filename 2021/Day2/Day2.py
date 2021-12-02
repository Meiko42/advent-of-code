def read_input(input_file):
    inputs = [x for x in open(input_file)]

    return inputs


def main():
    # input_file = "input-test.txt"
    input_file = "input.txt"

    inputs = read_input(input_file)
    print(inputs)

    horizontal_positon = 0
    depth_positon = 0
    aim = 0

    # for line in inputs:
    #     instruction = line.split()
    #     if instruction[0] == 'forward':
    #         horizontal_positon += int(instruction[1])
    #     if instruction[0] == 'down':
    #         depth_positon += int(instruction[1])
    #     if instruction[0] == 'up':
    #         depth_positon -= int(instruction[1])
    # part1 = horizontal_positon * depth_positon
    # print(part1)

    for line in inputs:
        instruction = line.split()
        if instruction[0] == 'forward':
            horizontal_positon += int(instruction[1])
            depth_positon += aim * int(instruction[1])
        if instruction[0] == 'down':
            aim += int(instruction[1])
        if instruction[0] == 'up':
            aim -= int(instruction[1])
    part2 = horizontal_positon * depth_positon
    print(part2)

if __name__ == "__main__":
    main()