#! /usr/bin/env python3

import os


testfile = "../tests/06.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.read().split('\n\n')]

inputfile = "../input/06.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.read().split('\n\n')]


def part1(answers):
    uniqueAnswers = [set(x.replace('\n', '')) for x in answers]
    return sum([len(x) for x in uniqueAnswers])


def part2(answers):
    commonResponse = 0
    for group in answers:
        allUniqueAnswers = set(group.replace('\n', ''))
        personAnswers = group.split('\n')
        for r in allUniqueAnswers:
            if all([r in a for a in personAnswers]):
                commonResponse += 1
    return commonResponse


if __name__ == '__main__':
    print("Tests:")
    print("Part 1:", part1(testInput))
    print("Part 2:", part2(testInput))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput))
    print("Part 2:", part2(myInput))
