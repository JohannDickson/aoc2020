#! /usr/bin/env python3

import os


testfile = "../tests/15.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [int(x) for x in f.read().strip().split(',')]

inputfile = "../input/15.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [int(x) for x in f.read().strip().split(',')]


def part1(numbers, turns):
    for i in range(len(numbers), turns):
        last = numbers[-1]

        if numbers.count(last) == 1:
            numbers.extend([0])

        elif numbers.count(last) > 1:
            lastSeen = list(reversed(numbers[:-1])).index(last) +1
            numbers.extend([lastSeen])

    return numbers[-1]


if __name__ == '__main__':
    print("Tests:")
    print("Part 1:", part1(testInput, 10))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput, 2020))
