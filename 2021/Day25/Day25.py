def read_input(input_file):
    inputs = [x.strip() for x in open(input_file)]

    new_inputs = []

    for line in inputs:
        new_inputs.append([char for char in line])

    return new_inputs


def check_if_east_moves(inputs):
    """Checks each East herd position, and returns
    the coordinates of positions that are able to move. """

    row_length = len(inputs[0]) - 1

    east_herd_moveable_coords = set()

    row_counter = 0
    for row in inputs:
        column_counter = 0
        for column in row:
            if column == ">":
                if column_counter == row_length:
                    if row[0] == ".":
                        east_herd_moveable_coords.add((row_counter, column_counter))
                else:
                    if row[column_counter + 1] == ".":
                        east_herd_moveable_coords.add((row_counter, column_counter))
            column_counter += 1
        row_counter += 1

    return east_herd_moveable_coords


def move_east(inputs):
    """Checks what positions can move east, and then moves them.
    Returns altered input where East herd has moved if possible, 
    and the number of moves that occcured. """

    east_herd_moveable_coords = check_if_east_moves(inputs)

    number_of_east_moves = len(east_herd_moveable_coords)

    if number_of_east_moves > 0:
        row_length = len(inputs[0]) - 1

        for coordinate in east_herd_moveable_coords:
            if (coordinate[1] + 1) > row_length:
                destination_coordinate = (coordinate[0], 0)
            else:
                destination_coordinate = (coordinate[0], coordinate[1] + 1)

            inputs[destination_coordinate[0]][destination_coordinate[1]] = ">"
            inputs[coordinate[0]][coordinate[1]] = "."

    return inputs, number_of_east_moves


def move_south(inputs):
    """Checks what positions can move east, and then moves them.
    Returns altered input where East herd has moved if possible, 
    and the number of moves that occcured. """
    
    south_herd_moveable_coords = check_if_south_moves(inputs)

    number_of_south_moves = len(south_herd_moveable_coords)

    if number_of_south_moves > 0:
        number_rows = len(inputs) - 1

        for coordinate in south_herd_moveable_coords:
            if (coordinate[0] + 1) > number_rows:
                destination_coordinate = (0, coordinate[1])
            else:
                destination_coordinate = (coordinate[0] + 1, coordinate[1])

            inputs[destination_coordinate[0]][destination_coordinate[1]] = "v"
            inputs[coordinate[0]][coordinate[1]] = "."

    return inputs, number_of_south_moves


    pass


def check_if_south_moves(inputs):
    """Checks each South herd position, and returns
    the coordinates of positions that are able to move. """

    number_rows = len(inputs) - 1

    south_herd_moveable_coords = set()

    row_counter = 0
    for row in inputs:
        column_counter = 0
        for column in row:
            if column == "v":
                if row_counter == number_rows:
                    if inputs[0][row_counter] == ".":
                        south_herd_moveable_coords.add((row_counter, column_counter))
                else:
                    if inputs[row_counter + 1][column_counter] == ".":
                        south_herd_moveable_coords.add((row_counter, column_counter))
            column_counter += 1
        row_counter += 1

    return south_herd_moveable_coords


def step(inputs):
    """A full "step" of movement for the herds.
    Move the East herd, then the South herd. 
    Returns the number of moves that happened in the step. """
    
    inputs, cucumber_east_moves = move_east(inputs)
    inputs, cucumber_south_moves = move_south(inputs)

    cucumber_moves = cucumber_east_moves + cucumber_south_moves

    return inputs, cucumber_moves

def main():
    input_file = "input-test.txt"
    # input_file = "input.txt"

    inputs = read_input(input_file)

    cucumber_moves = None
    number_of_steps = 0

    while (cucumber_moves != 0) and (number_of_steps < 2):
        inputs, cucumber_moves = step(inputs)

        number_of_steps += 1


    print(number_of_steps)
    for line in inputs:
        print(line)

if __name__ == "__main__":
    main()