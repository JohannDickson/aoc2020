#! /usr/bin/env python3

import os


# testfile = "../tests/10_1_1.txt"
testfile = "../tests/10_1_2.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [int(x.strip()) for x in f.readlines()]

inputfile = "../input/10.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [int(x.strip()) for x in f.readlines()]


def part1(adapters):
    maxRating = max(adapters)+3
    seatSocket = 0
    adapters = sorted([seatSocket]+adapters+[maxRating])
    joltDiffs = {1:0, 2:0, 3:0}

    for i in range(1, len(adapters)):
        joltDiffs[adapters[i] - adapters[i-1]] += 1

    return joltDiffs[1]*joltDiffs[3]


if __name__ == '__main__':
    print("Tests:")
    print("Part 1:", part1(testInput))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput))
