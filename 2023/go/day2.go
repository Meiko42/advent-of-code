package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type game struct {
	gameNum            int
	gameSets           map[int]map[string]int
	colorTotals        map[string]int
	colorMinimums      map[string]int
	colorMinimumsPower int
}

func readLines(filename string) ([]string, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return lines, nil
}

func parseGameInputLine(gameLine string) (game, error) {
	gameLineSplit := strings.Split(gameLine, ": ")

	newGame := new(game)

	var gameNumber int
	gameNumber, err := strconv.Atoi(strings.Split(gameLineSplit[0], " ")[1])

	gameSets := strings.Split(gameLineSplit[1], "; ")

	newGame.gameNum = gameNumber

	newGame.colorTotals = map[string]int{}
	newGame.colorMinimums = map[string]int{}
	newGame.gameSets = map[int]map[string]int{}

	for setNum, set := range gameSets {
		newGame.gameSets[setNum] = map[string]int{}
		colorsInSet := strings.Split(set, ", ")
		for _, colorValuesUnparsed := range colorsInSet {
			colorValues := strings.Split(colorValuesUnparsed, " ")
			var colorName string = colorValues[1]
			var colorNum int

			colorNum, _ = strconv.Atoi(colorValues[0])

			newGame.gameSets[setNum][colorName] = colorNum

			if val, ok := newGame.colorMinimums[colorName]; ok {
				if colorNum > val {
					newGame.colorMinimums[colorName] = colorNum
				}
			} else {
				newGame.colorMinimums[colorName] = colorNum
			}

			if val, ok := newGame.colorTotals[colorName]; ok {
				newVal := val + colorNum
				newGame.colorTotals[colorName] = newVal
			} else {
				newGame.colorTotals[colorName] = colorNum
			}
		}
	}

	newGame.colorMinimumsPower = 1

	for _, colorValue := range newGame.colorMinimums {
		newGame.colorMinimumsPower = newGame.colorMinimumsPower * colorValue
	}

	return *newGame, err
}

func main() {
	filename := "input.txt"

	lines, err := readLines(filename)
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}
	var part1 int = 0

	var part2 int = 0

	for _, line := range lines {
		var meetsConstraints bool = true
		game, _ := parseGameInputLine(line)
		part2 += game.colorMinimumsPower
		constraints := map[string]int{
			"red":   12,
			"green": 13,
			"blue":  14,
		}
		for constraintColor, constraintValue := range constraints {
			for _, setValues := range game.gameSets {
				if val, ok := setValues[constraintColor]; ok {
					if val > constraintValue {
						meetsConstraints = false
					}
				}
			}
		}
		if meetsConstraints {
			part1 += game.gameNum
		}
	}
	fmt.Println(part1)
	fmt.Println(part2)
}
