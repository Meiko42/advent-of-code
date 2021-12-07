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

def check_line_points(lineStart, lineEnd, linePoints, overlapCounter, stableX=None, stableY=None, otherLineStart=None, otherLineEnd=None):

    if (otherLineStart is None) and (lineStart > lineEnd):
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
        # In this case, lineStart=AX, lineEnd=BX, otherLineStart=AY, otherLineEnd=BY
        # Instructions say all lines are exactly 45 degrees. 
        xpos = lineStart
        ypos = otherLineStart
        origLineStart = lineStart
        origLineEnd = lineEnd
        if lineStart > lineEnd:
            temp = lineStart
            lineStart = lineEnd
            lineEnd = temp
        for i in range(lineStart, lineEnd+1):
            # print(len(range(lineStart, lineEnd+1)))
            print(xpos)
            print(ypos)
            if xpos not in linePoints:
                linePoints[xpos] = {}

            if ypos not in linePoints[xpos]:
                linePoints[xpos][ypos] = False
            else:
                linePoints[xpos][ypos] = True
                overlapCounter += 1
            
            if origLineStart > origLineEnd:
                xpos -= 1
            else:
                xpos += 1

            if otherLineStart > otherLineEnd:
                ypos -= 1
            else:
                ypos += 1

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
            # pass
            linePoints, overlapCounter = check_line_points(linePointAX, linePointBX, linePoints, overlapCounter, otherLineStart=linePointAY, otherLineEnd=linePointBY)

    pprint.pprint(linePoints)

    # print(overlapCounter)

    doubleCheckCounter = 0

    for x, values in linePoints.items():
        for y, hitcount in values.items():
            if hitcount:
                doubleCheckCounter += 1


    for x, values in linePoints.items():
        for i in range(0, 10):
            if i in values:
                if values[i]:
                    print("# ", end="", flush=True)
                else:
                    print(". ", end="", flush=True)
            else:
                print(". ", end="", flush=True)
        print()
        
    print(doubleCheckCounter)

if __name__ == "__main__":
    main()