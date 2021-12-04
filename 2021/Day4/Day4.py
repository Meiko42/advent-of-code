def read_input(input_file):
    inputs = [x.strip() for x in open(input_file)]

    return inputs


def check_cards(number_draw_list, boards, winning_boards):

    live_draw_list = []

    for i in number_draw_list:
        live_draw_list.append(int(i))
        # print(live_draw_list)

        if boards:
            for b in boards:
                for direction in b:
                    # print(direction)
                    # print()
                    # print(len(direction))
                    for numbers in direction:
                        matching_nums = 0
                        for num in numbers:
                            if int(num) in live_draw_list:
                                matching_nums +=1
                        if matching_nums == 5:
                            # print(len(direction))
                            insert = [direction, live_draw_list]
                            winning_boards.append(insert)
                            new_boards = boards
                            new_boards.remove(b)
                            return check_cards(number_draw_list, new_boards, winning_boards)
        else:
            return winning_boards


def main():
    # input_file = "input-test.txt"
    input_file = "input.txt"
    inputs = read_input(input_file)

    number_draw_list = inputs[0].split(',')

    input_loop = 2

    # [ [[rows], [columns]], [rows], [columns]], etc per board]
    boards = []
    card_rows = []
    for i in range(len(inputs)):
        if i > 1:
            if (inputs[i] != ''):
                card_rows.append(inputs[i].split())
            else:
                card_columns = []
                card_column = []
                col_counter = 0
                while col_counter != 5:
                    for i in card_rows:
                        card_column.append(i[col_counter])
                    col_counter += 1
                    card_columns.append(card_column)
                    card_column = []
                boards.append([card_rows, card_columns])
                card_rows = []
    # Awful fix to get last card
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
    


    winning_card = check_cards(number_draw_list, boards, [])


    longest = 0

    loser = None

    for cardinfo in winning_card:
        if len(cardinfo[1]) > longest:
            longest = len(cardinfo[1])
            loser = cardinfo

    # print(loser)

    sum_unmarked = 0

    for row in loser[0]:
        for i in row:
            if int(i) not in loser[1]:
                print(i)
                sum_unmarked = sum_unmarked + int(i)

    # print(sum_unmarked)

    
    print(sum_unmarked * loser[1][-1])

    # for i in winning_card:

    # print(called_numbers)

    # sum_unmarked = 0

    # for row in winning_card[0]:
    #     for i in row:
    #         if int(i) not in called_numbers:
    #             sum_unmarked = sum_unmarked + int(i)

    # print(sum_unmarked * called_numbers[-1])


if __name__ == "__main__":
    main()