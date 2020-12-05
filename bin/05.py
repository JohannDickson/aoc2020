#! /usr/bin/env python3

import os


testfile = "../tests/05.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/05.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]


def part1(boardingPasses):
    # Did this manually,
    # Binary representation, F/L = 0, B/R = 1
    return boardingPasses


if __name__ == '__main__':
    print("Tests:")
    print("Part 1:", part1(testInput))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput))
