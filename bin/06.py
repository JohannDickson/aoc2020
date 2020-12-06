#! /usr/bin/env python3

import os


testfile = "../tests/06.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.replace('\n', '').strip() for x in f.read().split('\n\n')]

inputfile = "../input/06.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.replace('\n', '').strip() for x in f.read().split('\n\n')]


def part1(answers):
    uniqueAnswers = [set(x) for x in answers]
    return sum([len(x) for x in uniqueAnswers])


if __name__ == '__main__':
    print("Tests:")
    print("Part 1:", part1(testInput))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput))
