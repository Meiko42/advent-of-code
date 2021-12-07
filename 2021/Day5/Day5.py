import pprint

def read_input(input_file):
    inputs = [x.strip().split(' -> ') for x in open(input_file)]

    return inputs


# def check_line_points(lineStart, lineEnd, linePoints, overlappingLinePoints):

#     if lineStart < lineEnd:
#         temp = lineStart
#         lineStart = lineEnd
#         lineEnd = temp

#     linePosition = lineStart
#     for i in range(lineStart, lineEnd + 1):
#         print(linePosition)
#         if linePosition not in linePoints:
#             linePoints.add(linePosition)
#         elif linePosition in linePoints:
#             overlappingLinePoints.add(linePosition)
#         else:
#             raise Exception("""We shouldn't be able to reach this point""")

#         linePosition += 1
#     print(linePoints)
#     print(overlappingLinePoints)
#     return linePoints, overlappingLinePoints

def check_line_points(lineStart, lineEnd, linePoints, overlapCounter, stableX=None, stableY=None):

    if lineStart > lineEnd:
        temp = lineStart
        lineStart = lineEnd
        lineEnd = temp

    if stableX:
        if stableX not in linePoints:
            linePoints[stableX] = {}
        for i in range(lineStart, lineEnd+1):
            if i not in linePoints[stableX]:
                linePoints[stableX][i] = False
            else:
                linePoints[stableX][i] = True
                overlapCounter += 1
    elif stableY:
        for i in range(lineStart, lineEnd+1):
            if i not in linePoints:
                linePoints[i] = {}
            if stableY not in linePoints[i]:
                linePoints[i][stableY] = False
            else:
                linePoints[i][stableY] = True
                overlapCounter += 1
    else:
        raise Exception('Incorrect values supplied to check_line_points.')

    return linePoints, overlapCounter

def main():
    # input_file = "input-test.txt"
    input_file = "input.txt"
    inputs = read_input(input_file)

    # print(inputs)

    linePoints = {}
    overlapCounter = 0

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
            linePoints, overlapCounter = check_line_points(linePointAY, linePointBY, linePoints, overlapCounter, stableX=linePointAX)
        elif linePointAY == linePointBY:
            linePoints, overlapCounter = check_line_points(linePointAX, linePointBX, linePoints, overlapCounter, stableY=linePointAY)
        else:
            # print(f"Skipping diaganal line: {line}")
            pass

    # pprint.pprint(linePoints)

    # print(overlapCounter)

    doubleCheckCounter = 0

    for x, values in linePoints.items():
        for y, hitcount in values.items():
            if hitcount:
                doubleCheckCounter += 1
    
    print(doubleCheckCounter)

if __name__ == "__main__":
    main()