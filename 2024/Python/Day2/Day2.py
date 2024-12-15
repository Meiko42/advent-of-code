#!/usr/bin/env python3

def safety_check(report):
    """Returns True if a report is safe"""

    priorValue = None
    priorSlope = None

    for level in map(int, report.split()):
        if not priorValue:
            priorValue = level
            continue

        # if negative, we are increasing from left to right
        # if positive, we are decreasing from left to right
        slope = priorValue - level

        if not priorSlope:
            priorSlope = slope

        if (1 > abs(slope)) or (abs(slope) > 3):
            return False

        # Check consistency of slope direction
        if slope > 0:
            if not ((slope > 0) and (priorSlope > 0)):
                return False

        if slope < 0:
            if not ((slope < 0) and (priorSlope < 0)):
                return False

        priorValue = level
        priorSlope = slope

    return True


def main():

    safeReports = 0

    with open("input", "r") as inputFile:
        for report in inputFile:
            if safety_check(report):
                safeReports += 1

    print(f"Part one answer: {safeReports}")


if __name__ == "__main__":
    main()
