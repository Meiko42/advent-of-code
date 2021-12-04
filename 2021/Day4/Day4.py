def read_input(input_file):
    inputs = [x.strip() for x in open(input_file)]

    return inputs


def check_cards(number_draw_list, boards):

    live_draw_list = []

    winning_board = []

    for i in number_draw_list:
        live_draw_list.append(i)

        for b in boards:
            for direction in b:
                for numbers in direction:
                    matching_nums = 0
                    for num in numbers:
                        if num in live_draw_list:
                            matching_nums +=1
                    if matching_nums == 5:
                        return b


def main():
    input_file = "input-test.txt"
    # input_file = "input.txt"
    inputs = read_input(input_file)

    number_draw_list = inputs[0].split(',')

    input_loop = 2

    # [ [[rows], [columns]], [rows], [columns]], etc per board]
    boards = []
    card_rows = []
    for i in range(len(inputs)):
        if i > 1:
            if inputs[i] != '':
                card_rows.append(inputs[i].split())
            else:
                card_columns = []
                card_column = []
                col_counter = 0
                while col_counter != 4:
                    for i in card_rows:
                        card_column.append(i[col_counter])
                    col_counter += 1
                    card_columns.append(card_column)
                    card_column = []
                boards.append([card_rows, card_columns])
                card_rows = []


    winning_card = check_cards(number_draw_list, boards)
    print(winning_card)


if __name__ == "__main__":
    main()