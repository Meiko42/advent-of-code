def read_input(input_file):
    inputs = []

    with open(input_file) as opened_input_file:
        for line in opened_input_file:
            inputs.append([int(x) for x in line.strip()])

    return inputs


def increase_surrounding_positions(inputs, coordinate_tuple):
    """Increases all positions around a flash by 1"""

    num_lines = len(inputs) - 1
    line_length = len(inputs[0]) - 1

    x = coordinate_tuple[0]
    y = coordinate_tuple[1]

    if x > 0:
        inputs[x-1][y] += 1

    if x < num_lines:
        inputs[x+1][y] += 1

    if y > 0:
        inputs[x][y-1] += 1

    if y < line_length:
        inputs[x][y+1] += 1
    
    if (x < num_lines) and (y < line_length):
        inputs[x+1][y+1] += 1

    if (x < num_lines) and (y > 0):
        inputs[x+1][y-1] += 1

    if (x > 0) and (y < line_length):
        inputs[x-1][y+1] += 1

    if (x > 0) and y > 0:
        inputs[x-1][y-1] += 1

    # x+1, y
    # x-1, y
    # x, y+1
    # x, y-1
    # x+1, y+1
    # x+1, y-1
    # x-1, y+1
    # x-1, y-1

    return inputs

def set_flashed_positions_to_zero(inputs, flashed_positions):

    for position in flashed_positions:
        inputs[position[0]][position[1]] = 0

    return inputs


def evaluate_all_flashes(inputs, positions_to_flash, all_flashed_positions):
    """Expects input that has already been incremented by 1.
    Also expects set of initial positions_to_flash.
    This is intended to be recursive - will call ourself until 
    there are no new flashes detected. We will return the new input, 
    and a set of all positions (x, y) that flashed. """

    # print(positions_to_flash)

    for flash_coordinate in positions_to_flash:
        inputs = increase_surrounding_positions(inputs, flash_coordinate)

    for position in positions_to_flash:
        all_flashed_positions.add(position)

    positions_to_flash = set()

    line_counter = 0
    for line in inputs:
        position_counter = 0
        for position in line:
            if (position > 9) and ((line_counter, position_counter) not in all_flashed_positions):
                positions_to_flash.add((line_counter, position_counter))
            position_counter += 1
        line_counter += 1

    if len(positions_to_flash) > 0:
        inputs, all_flashed_positions = evaluate_all_flashes(inputs, positions_to_flash, all_flashed_positions)

    # print(f"Existing flashed positions: {positions_to_flash}")
    # print(f"Positions that need to flash: {positions_to_flash}")


    return inputs, all_flashed_positions


def increment_all_by_one(inputs):

    modified_inputs = []

    initial_flashes = set()

    line_counter = 0
    for line in inputs:
        position_counter = 0
        modified_inputs.append([])
        for position in line:
            position += 1
            modified_inputs[line_counter].append(position)

            if position > 9:
                initial_flashes.add((line_counter, position_counter))
            position_counter += 1
        line_counter += 1

    return modified_inputs, initial_flashes


def part_one(inputs):

    number_of_flashes = 0

    iterations = 1

    while True:

        # print(f"Step {i}:")

        inputs, initial_flashes = increment_all_by_one(inputs)

        # print("Increased all by 1:")
        # for line in inputs:
        #     print(line)

        inputs, flashed_positions = evaluate_all_flashes(inputs, initial_flashes, set())

        number_of_flashes += len(flashed_positions)

        inputs = set_flashed_positions_to_zero(inputs, flashed_positions)

        # print("Increased areas surrounding flashes by 1:")
        # for line in inputs:
        #     print(line)

        # print(iterations)
        if iterations == 100:
            print(number_of_flashes)

        if len(flashed_positions) == 100:
            print(iterations)
            return

        iterations += 1


def main():
    # input_file = "input-test.txt"
    input_file = "input.txt"

    inputs = read_input(input_file)

    part_one(inputs)


if __name__ == "__main__":
    main()