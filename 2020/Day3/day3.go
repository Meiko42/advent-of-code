package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
)

func slopeCheck(inputSlice []string, lineLength int, overNum int, downNum int) (treesCounter int, err error) {
	pointer := 0
	downCounter := 0
	for _, line := range inputSlice {
		modVal := downCounter % downNum
		if modVal == 0 {
			if string([]rune(line)[pointer]) == "#" {
				treesCounter = treesCounter + 1
			}
			pointer = pointer + overNum
			if pointer >= lineLength {
				pointer = pointer % lineLength
			}
		}
		downCounter++
	}
	return
}

func main() {
	inputFile, inputFileError := os.Open("./Input.txt")

	part2InputFile, part2InputFileError := os.Open("./part2Input.txt")

	if (inputFileError != nil) || (part2InputFileError != nil) {
		log.Fatalf("Error while opening files! \n%s\n%s", inputFileError, part2InputFileError)
	}

	scanner1 := bufio.NewScanner(inputFile)

	var inputSlice []string
	var lineLen int
	for scanner1.Scan() {
		inputSlice = append(inputSlice, scanner1.Text())
		lineLen = len(scanner1.Text())
	}

	inputList2Parse := regexp.MustCompile("^Right (\\d), down (\\d)")

	// Part 1:
	part1Trees, part1Error := slopeCheck(inputSlice, lineLen, 3, 1)

	if part1Error == nil {
		// Part 1 Answer: 268
		fmt.Printf("\nPart 1 Answer: %d\n", part1Trees)
	} else {
		log.Fatal(part1Error)
	}

	// Part 2:
	scanner2 := bufio.NewScanner(part2InputFile)

	var part2ValuesSlice []int
	for scanner2.Scan() {
		input := inputList2Parse.FindSubmatch(scanner2.Bytes())
		// Relying on the regex match, ignoring err
		input1, _ := strconv.Atoi(string(input[1]))
		input2, _ := strconv.Atoi(string(input[2]))
		trees, err := slopeCheck(inputSlice, lineLen, input1, input2)
		if err == nil {
			part2ValuesSlice = append(part2ValuesSlice, trees)
		} else {
			log.Fatal(err)
		}
	}
	part2Answer := 1
	for _, value := range part2ValuesSlice {
		part2Answer = part2Answer * value
	}
	fmt.Printf("Part 2 Individual Values: %d\n", part2ValuesSlice)
	fmt.Printf("Part 2 Answer: %d\n", part2Answer)
}
