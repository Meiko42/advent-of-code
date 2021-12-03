def read_input(input_file):
    inputs = [x.strip() for x in open(input_file)]

    return inputs


def recurse_check_oxy(inputs, preferred_bit, position):

    preferred_bit_orig = preferred_bit
    new_list = []

    counter = 0
    list_length = len(inputs)

    for entry in inputs:
        if entry[position] == '1':
            counter += 1

    if counter > (list_length / 2):
        preferred_bit = 1
    elif counter < (list_length / 2):
        preferred_bit = 0

    for entry in inputs:
        if entry[position] == str(preferred_bit):
            new_list.append(entry)

    # print(new_list)
    if len(new_list) is 1:
        return new_list[0]
    else:
        position += 1
        # print(new_list)
        return recurse_check_oxy(new_list, preferred_bit_orig, position)


def recurse_check_scr(inputs, preferred_bit, position):

    preferred_bit_orig = preferred_bit
    new_list = []

    counter = 0
    list_length = len(inputs)

    for entry in inputs:
        if entry[position] == '1':
            counter += 1

    if counter > (list_length / 2):
        preferred_bit = 0
    elif counter < (list_length / 2):
        preferred_bit = 1

    for entry in inputs:
        if entry[position] == str(preferred_bit):
            new_list.append(entry)

    # print(new_list)
    if len(new_list) is 1:
        return new_list[0]
    else:
        position += 1
        # print(new_list)
        return recurse_check_scr(new_list, preferred_bit_orig, position)


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

    # print(epsilon)

    print(int(epsilon, 2) * int(gamma, 2))


    oxygen_generator = recurse_check_oxy(inputs, 1, 0)
    scrubber_rating = recurse_check_scr(inputs, 0, 0)

    # print(int(oxygen_generator, 2))
    # print(int(scrubber_rating, 2))

    print(int(oxygen_generator, 2) * int(scrubber_rating, 2))

    # print(int(oxygen_generator, 2) * int(scrubber_rating, 2))


    # print(inputs)


if __name__ == "__main__":
    main()