package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
)

func part1(regexpMatch []string) (valid bool, err error) {
	charCounter := 0

	for _, character := range regexpMatch[4] {
		if string(character) == regexpMatch[3] {
			charCounter++
		}
	}
	// Regex matched correctly if we've made it this far,
	// confident Atoi will succeed.
	condition1, _ := strconv.Atoi(regexpMatch[1])
	condition2, _ := strconv.Atoi(regexpMatch[2])
	if charCounter >= condition1 && charCounter <= condition2 {
		valid = true
	}

	return
}

func part2(regexpMatch []string) (valid bool, err error) {
	charCounter := 0
	// Regex matched correctly if we've made it this far,
	// confident Atoi will succeed.
	position1, _ := strconv.Atoi(regexpMatch[1])
	position2, _ := strconv.Atoi(regexpMatch[2])
	position1 = position1 - 1
	position2 = position2 - 1

	if string(regexpMatch[4][position1]) == regexpMatch[3] {
		charCounter++
	}
	if string(regexpMatch[4][position2]) == regexpMatch[3] {
		charCounter++
	}
	if charCounter == 1 {
		valid = true
	}

	return
}

func main() {
	inputParse := regexp.MustCompile("^(\\d+)-(\\d+) (\\S): (.+)")

	inputFile, error := os.Open("./Input.txt")

	if error != nil {
		log.Fatal(error)
	}

	scanner := bufio.NewScanner(inputFile)

	var goodPassCount int = 0
	var goodPassCount2 int = 0

	for scanner.Scan() {
		regexpMatch := inputParse.FindStringSubmatch(scanner.Text())

		if regexpMatch == nil {
			fatalError := fmt.Sprintf("\nBad input line: \"%s\"\nHalting", scanner.Text())
			log.Fatal(fatalError)
		}

		if valid, _ := part1(regexpMatch); valid {
			goodPassCount++
		}
		if valid, _ := part2(regexpMatch); valid {
			goodPassCount2++
		}
	}

	//Part 1 Answer: 614
	fmt.Printf("Part 1 Answer: %d \n", goodPassCount)

	//Part 2 Answer: 354
	fmt.Printf("Part 2 Answer: %d \n", goodPassCount2)

}
