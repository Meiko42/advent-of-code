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


def modelSeating(seatingRowsList):
    newSeatingRowsList = copy.deepcopy(seatingRowsList)
    rowCounter = 0
    changes = 0

    for row in seatingRowsList:
        rowLen = len(row) - 1
        seatCounter = 0
        while seatCounter <= rowLen:
            if row[seatCounter] == "L":
                adjacentResults = findAdjacentSeatValues(seatingRowsList, rowCounter, seatCounter)
                if adjacentResults.count("#") == 0:
                    newSeatingRowsList[rowCounter][seatCounter] = "#"
                    changes += 1
            elif row[seatCounter] == "#":
                adjacentResults = findAdjacentSeatValues(seatingRowsList, rowCounter, seatCounter)
                if adjacentResults.count("#") >= 4:
                    newSeatingRowsList[rowCounter][seatCounter] = "L"
                    changes += 1
            seatCounter += 1
        rowCounter += 1

    return newSeatingRowsList, changes

changes = 1

while changes != 0:
    initialSeatingRowsList, changes = modelSeating(initialSeatingRowsList)

occupiedSeats = 0 

for row in initialSeatingRowsList:
    rowPrint = ""
    for seat in row:
        rowPrint = rowPrint + str(seat)
        if seat == "#":
            occupiedSeats += 1
    print(rowPrint)

print(f"\nOccupied Seats: {occupiedSeats}\n")
