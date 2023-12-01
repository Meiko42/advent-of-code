

# So yeah, it's kinda awful.
# Doing this at 1am after a long workday and being out for a couple drinks wasn't a great idea.
# Will re-do this later.

def read_input(input_file):
    inputs = [str(x.strip()) for x in open(input_file)]

    return inputs

def part1(inputs):
    answer = 0
    newlines = []
    for line in inputs:
        newline = ""
        for char in line:
            try:
                if int(char):
                    newline += str(char)
            except:
                pass
        number = str(newline[0]) + str(newline[-1])
        answer += int(number)
        
    print(answer)

def part2(inputs):
    num_words = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    fixed_inputs = []

    for line in inputs:
        scan = ""
        newline = ""
        newscan = ""
        for char in line:
            try:
                if int(char):
                    newline += str(char)
            except:
                scan += str(char)
                for word, num in num_words.items():
                    newscan = scan.replace(word, str(num))
                    if scan != newscan:
                        newline += str(newscan)
                        scan = ""
                        newscan = ""
                        
        scan = ""
        reverseline = ""
        newscan = ""

        for char in reversed(line):
            try:
                if int(char):
                    reverseline += str(char)
            except:
                scan =  str(char) + scan
                for word, num in num_words.items():
                    newscan = scan.replace(word, str(num))
                    if scan != newscan:
                        reverseline += str(newscan)
                        scan = ""
                        newscan = ""

        for char in reversed(reverseline):
            newline += str(char)
            
    
        fixed_inputs.append(newline)

    part1(fixed_inputs)


def main():
    input_file = "input.txt"
    inputs = read_input(input_file)
    part1(inputs)
    part2(inputs)

if __name__ == "__main__":
    main()