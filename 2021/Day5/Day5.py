def read_input(input_file):
    inputs = [x.strip().split(' -> ') for x in open(input_file)]

    return inputs


def check_line_points(lineStart, lineEnd, linePoints, overlappingLinePoints):

    print(lineStart)
    print(lineEnd)
    
    position = lineStart
    for i in range(lineStart, lineEnd + 1):
        # print(position)
        if position not in linePoints:
            linePoints.add(position)
        elif position in linePoints:
            overlappingLinePoints.add(position)
        else:
            raise Exception("""We shouldn't be able to reach this point""")
        position += 1

    return linePoints, overlappingLinePoints


def main():
    input_file = "input-test.txt"
    # input_file = "input.txt"
    inputs = read_input(input_file)

    # print(inputs)

    linePoints = set()
    overlappingLinePoints = set()

    for line in inputs:
        linePointA = line[0].split()
        linePointZ = line[1].split()
        linePointA = linePointA[0]
        linePointZ = linePointZ[0]
        linePointA = linePointA.split(',')
        linePointZ = linePointZ.split(',')
        linePointAX = int(linePointA[0])
        linePointAY = int(linePointA[1])
        linePointBX = int(linePointZ[0])
        linePointBY = int(linePointZ[1])
        if linePointAX == linePointBX:
            linePoints, overlappingLinePoints = check_line_points(linePointAY, linePointBY, linePoints, overlappingLinePoints)
        if linePointAY == linePointBY:
            linePoints, overlappingLinePoints = check_line_points(linePointAX, linePointBX, linePoints, overlappingLinePoints)

    print(len(overlappingLinePoints))

if __name__ == "__main__":
    main()