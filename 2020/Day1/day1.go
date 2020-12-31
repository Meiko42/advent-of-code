package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func partOne(inputMap map[int32]int32) string {
	var part1Slice []int32

	for _, v := range inputMap {
		if _, found := inputMap[v]; found {
			part1Slice = append(part1Slice, v)
		}
	}

	part1Answer := part1Slice[0] * part1Slice[1]
	answer1String := fmt.Sprintf("Part 1 - Found %d and %d\nAnswer is %d\n", part1Slice[0], part1Slice[1], part1Answer)
	return answer1String
}

func partTwo(inputMap map[int32]int32) string {
	for k1 := range inputMap {
		for k2 := range inputMap {
			for k3 := range inputMap {
				if k1+k2+k3 == 2020 {
					part2Answer := k1 * k2 * k3
					answer2String := fmt.Sprintf("Part 2 - Found %d, %d and %d\nAnswer is %d\n", k1, k2, k3, part2Answer)
					return answer2String
				}
			}
		}
	}
	return "There is no match for part 2"
}

func main() {
	inputFile, error := os.Open("./Input.txt")

	if error != nil {
		log.Fatal(error)
	}

	scanner := bufio.NewScanner(inputFile)

	// Holds input lines as keys and compliment as value
	inputMap := make(map[int32]int32)

	for scanner.Scan() {
		inputInt, _ := strconv.Atoi(scanner.Text())
		inputMap[int32(inputInt)] = 2020 - int32(inputInt)
	}

	// Answer:
	// Part 1: Found 1477, 543
	// Part 1: Answer is 802011
	fmt.Print(partOne(inputMap))

	// Answer:
	// Part 2: Found 422, 577, 1021
	// Part 2: Answer is 248607374
	fmt.Print(partTwo(inputMap))

}
