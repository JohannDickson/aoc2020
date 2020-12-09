#! /usr/bin/env python3

import os


testfile = "../tests/09.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [int(x.strip()) for x in f.readlines()]

inputfile = "../input/09.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [int(x.strip()) for x in f.readlines()]


def isValid(number, previous):
    for i in previous:
        for j in previous:
            if i!=j and i+j==number:
                return True
    return False


def part1(xmas, lookback):
    for i in range(lookback, len(xmas)):
        if not isValid(xmas[i], xmas[i-lookback:i]):
            return xmas[i]
    return False


if __name__ == '__main__':
    print("Tests:")
    print("Part 1:", part1(testInput, 5))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput, 25))
