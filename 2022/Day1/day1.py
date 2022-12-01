from pprint import pprint


perElfFood = {}
elf = 1
largestNum = 0
with open("input") as inputfile:
    for line in inputfile:
        line = line.strip()
        if line:
            if elf not in perElfFood.keys():
                perElfFood[elf] = 0
            perElfFood[elf] += int(line)
        else:
            if perElfFood[elf] > largestNum:
                largestNum = perElfFood[elf]
            elf += 1

print(largestNum)

caloriesList = []
for elf, calories in perElfFood.items():
    caloriesList.append(calories)

caloriesList.sort(reverse=True)

pprint(caloriesList)

print(caloriesList[0] + caloriesList[1] + caloriesList[2])