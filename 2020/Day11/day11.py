import copy

# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.
# Floor (.) never changes; seats don't move, and nobody sits on the floor.


initialSeatingRowsList = []

with open("Input.txt") as inputFile:
    for line in inputFile:
        line = line.strip()
        seatingColumnList = []
        for char in line:
            seatingColumnList.append(char)
        initialSeatingRowsList.append(seatingColumnList)

def findAdjacentSeatValues2(seatingRowsList, row, seat):
    numRows = len(seatingRowsList) - 1
    numRowsRange = len(seatingRowsList)
    rowLen = len(seatingRowsList[row]) - 1
    rowLenRange = len(seatingRowsList[row])
    rowBehind = row - 1
    rowAhead = row + 1
    seatBehind = seat - 1
    seatAhead = seat + 1
    adjacentList = [[
        rowBehind, seatBehind, -1, -1
    ], [
        rowBehind, seat, -1, 0
    ], [
        rowBehind, seatAhead, -1, 1
    ], [
        row, seatBehind, 0, -1
    ], [
        row, seatAhead, 0, 1
    ], [
        rowAhead, seatBehind, 1, -1
    ], [
        rowAhead, seat, 1, 0
    ], [
        rowAhead, seatAhead, 1, 1]]
    adjacentResults = []

    for adjacency in adjacentList:
        rowSearch = adjacency[0]
        seatSearch = adjacency[1]
        
        found = False

        while (rowSearch in range(0, numRowsRange)) and (seatSearch in range(0, rowLenRange) and (found is False)):
            if seatingRowsList[rowSearch][seatSearch] == ".":
                rowSearch += adjacency[2]
                seatSearch += adjacency[3]
            else: 
                found = True
                # print(f"Row: {rowSearch}, Seat: {seatSearch}")
                adjacentResults.append(seatingRowsList[rowSearch][seatSearch])
        # adjacentResults.append(seatingRowsList[rowSearch][seatSearch])

    return adjacentResults


def findAdjacentSeatValues(seatingRowsList, row, seat):
    numRows = len(seatingRowsList) - 1
    numRowsRange = len(seatingRowsList)
    rowLen = len(seatingRowsList[row]) - 1
    rowLenRange = len(seatingRowsList[row])
    rowBehind = row - 1
    rowAhead = row + 1
    seatBehind = seat - 1
    seatAhead = seat + 1
    adjacentList = [[
        rowBehind, seatBehind
    ], [
        rowBehind, seat
    ], [
        rowBehind, seatAhead
    ], [
        row, seatBehind
    ], [
        row, seatAhead
    ], [
        rowAhead, seatBehind
    ], [
        rowAhead, seat
    ], [
        rowAhead, seatAhead]]
    adjacentResults = []

    for adjacency in adjacentList:
        if (adjacency[0] in range(0, numRowsRange)) and (adjacency[1] in range(0, rowLenRange)):
            adjacentResults.append(seatingRowsList[adjacency[0]][adjacency[1]])

    return adjacentResults


def modelSeating(seatingRowsList, tolerance, farSight):
    newSeatingRowsList = copy.deepcopy(seatingRowsList)
    rowCounter = 0
    changes = 0

    for row in seatingRowsList:
        rowLen = len(row) - 1
        seatCounter = 0
        while seatCounter <= rowLen:
            if row[seatCounter] == "L":
                if farSight is False: 
                    adjacentResults = findAdjacentSeatValues(seatingRowsList, rowCounter, seatCounter)
                if farSight is True: 
                    adjacentResults = findAdjacentSeatValues2(seatingRowsList, rowCounter, seatCounter)
                if adjacentResults.count("#") == 0:
                    newSeatingRowsList[rowCounter][seatCounter] = "#"
                    changes += 1
            elif row[seatCounter] == "#":
                if farSight is False: 
                    adjacentResults = findAdjacentSeatValues(seatingRowsList, rowCounter, seatCounter)
                if farSight is True: 
                    adjacentResults = findAdjacentSeatValues2(seatingRowsList, rowCounter, seatCounter)
                if adjacentResults.count("#") >= tolerance:
                    newSeatingRowsList[rowCounter][seatCounter] = "L"
                    changes += 1
            seatCounter += 1
        rowCounter += 1

    return newSeatingRowsList, changes

changes = 1

part1SeatingRowsList = copy.deepcopy(initialSeatingRowsList)
part2SeatingRowsList = copy.deepcopy(initialSeatingRowsList)

while changes != 0:
    part1SeatingRowsList, changes = modelSeating(part1SeatingRowsList, 4, False)

occupiedSeats = 0 

for row in part1SeatingRowsList:
    rowPrint = ""
    for seat in row:
        rowPrint = rowPrint + str(seat)
        if seat == "#":
            occupiedSeats += 1
    print(rowPrint)

# Part 1 - Answer 2386
print(f"\nOccupied Seats: {occupiedSeats}\n")

changes = 1
while changes != 0:
    part2SeatingRowsList, changes = modelSeating(part2SeatingRowsList, 5, True)

occupiedSeats = 0 

for row in part2SeatingRowsList:
    rowPrint = ""
    for seat in row:
        rowPrint = rowPrint + str(seat)
        if seat == "#":
            occupiedSeats += 1
    print(rowPrint)

# Part 2 - Answer 2091
print(f"\nOccupied Seats: {occupiedSeats}\n")