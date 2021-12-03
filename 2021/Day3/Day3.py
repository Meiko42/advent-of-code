def read_input(input_file):
    inputs = [x.strip() for x in open(input_file)]

    return inputs


def main():
    # input_file = "input-test.txt"
    input_file = "input.txt"
    inputs = read_input(input_file)

    gamma = ''
    epsilon = ''

    for line in inputs:
        line_length = len(line)

    input_list_length = len(inputs)

    for x in range(line_length):
        counter = 0
        for line in inputs:
            if line[x] == '1':
                counter += 1
        if (counter) > (input_list_length / 2):
            gamma = gamma + '1'
        else:
            gamma = gamma + '0'

    print(gamma)

    for i in gamma:
        if i == '1':
            epsilon = epsilon + '0'
        else:
            epsilon = epsilon + '1'

    print(epsilon)

    print(int(epsilon, 2) * int(gamma, 2))


    # print(inputs)


if __name__ == "__main__":
    main()