def read_input(input_file):
    inputs = [x.strip() for x in open(input_file)]

    return inputs


def main():
    input_file = "input-test.txt"
    input_file = "input.txt"
    inputs = read_input(input_file)

    num_lines = len(inputs) - 1
    line_length = len(inputs[0]) - 1


    risk_level = 0

    line_counter = 0
    for line in inputs:
        value_counter = 0
        for value in line:
            value = int(value)
            passed = True
            #check neighbors on same line
            print(value)

            print(f"value_counter is {value_counter}")
            if value_counter != 0:
                if value >= int(line[value_counter - 1]):
                    passed = False
                print(int(line[value_counter - 1]))

            if value_counter < line_length:
                if value >= int(line[value_counter + 1]):
                    passed = False
                print(int(line[value_counter + 1]))

            # check neighbors on other lines
            if line_counter != 0:
                if value >= int(inputs[line_counter - 1][value_counter]):
                    passed = False
                print(int(inputs[line_counter - 1][value_counter]))

            if line_counter < num_lines:
                if value >= int(inputs[line_counter + 1][value_counter]):
                    passed = False
                print(int(inputs[line_counter + 1][value_counter]))

            if passed:
                risk_level += 1 + value
                print("HIT")
            value_counter += 1

            print()
        line_counter += 1


    # 1582 is NOT correct. It's too high
    # 438 is NOT correct. It's too low (changed from > to >= matching)
    print(risk_level)


if __name__ == "__main__":
    main()