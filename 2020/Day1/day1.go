package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

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

	// This should stop after the first match and record the k, v
	// For now just appending to slice
	var part1Slice []int32

	for _, v := range inputMap {
		if _, found := inputMap[v]; found {
			part1Slice = append(part1Slice, v)
		}
	}

	part1Answer := part1Slice[0] * part1Slice[1]

	answer1String := fmt.Sprintf("Found %d and %d\nAnswer is %d\n", part1Slice[0], part1Slice[1], part1Answer)

	fmt.Print(answer1String)

}
