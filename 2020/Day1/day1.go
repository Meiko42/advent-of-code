package main

import (
	"bufio"
	"errors"
	"fmt"
	"log"
	"os"
	"strconv"
)

func partOne(inputMap map[int32]int32) (answer1String string, err error) {
	defer func() {
		if answer1String == "" {
			err = errors.New("There is no match for part 1")
		}
	}()

	for _, v := range inputMap {
		if v2, found := inputMap[v]; found {
			part1Answer := v * v2
			answer1String = fmt.Sprintf("Part 1 - Found %d and %d\nAnswer is %d\n", v, v2, part1Answer)
			return
		}
	}

	return
}

func partTwo(inputMap map[int32]int32) (answer2String string, err error) {
	defer func() {
		if answer2String == "" {
			err = errors.New("There is no match for part 2")
		}
	}()

	for k1 := range inputMap {
		for k2 := range inputMap {
			for k3 := range inputMap {
				if k1+k2+k3 == 2020 {
					part2Answer := k1 * k2 * k3
					answer2String = fmt.Sprintf("Part 2 - Found %d, %d and %d\nAnswer is %d\n", k1, k2, k3, part2Answer)
					return
				}
			}
		}
	}

	return
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
	if part1Answer, part1Error := partOne(inputMap); part1Error != nil {
		log.Fatal(part1Error)
	} else {
		fmt.Print(part1Answer)
	}

	// Answer:
	// Part 2: Found 422, 577, 1021
	// Part 2: Answer is 248607374
	if part2Answer, part2Error := partTwo(inputMap); part2Error != nil {
		log.Fatal(part2Error)
	} else {
		fmt.Print(part2Answer)
	}
}
