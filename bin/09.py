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


def part2(xmas, lookback):
    invalidNumber = part1(xmas, lookback)
    for i in range(len(xmas)):
        contiguousSum = 0
        for x in range(i, len(xmas)):
            contiguousSum += xmas[x]
            if contiguousSum > invalidNumber:
                continue
            elif contiguousSum == invalidNumber:
                contiguous = xmas[i:x]
                lower = min(contiguous)
                upper = max(contiguous)
                return lower+upper
    return False


if __name__ == '__main__':
    print("Tests:")
    print("Part 1:", part1(testInput, 5))
    print("Part 2:", part2(testInput, 5))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput, 25))
    print("Part 2:", part2(myInput, 25))
