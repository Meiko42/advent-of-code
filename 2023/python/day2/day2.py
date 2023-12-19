from pprint import pprint

def read_inputs(input_file):
	input_lines = [x.strip() for x in open(input_file, "r")]
	return input_lines

def part1(input_lines):
    # Process each game against constraints
    # add up the values of the game numbers that would have been possible.

    constraints_dict = {"red": 12, "green": 13, "blue": 14}
    constraint_total_cubes = 0
    constraint_total_cubes = constraint_total_cubes + y for y in constraints_dict.keys()

	for game in input_lines:
		game_number, game_reveals = game.split(":")
		game_number = game_number.split(" ")[1]
		game_reveals = [x for x in game_reveals.split(";")]

		pprint(game_number)
		pprint(game_reveals)

def main():

	input_lines = read_inputs("input.txt")
	# pprint(input_lines)
	part1(input_lines)

if __name__ == "__main__":
	main()
