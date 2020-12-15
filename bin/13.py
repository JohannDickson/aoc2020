#! /usr/bin/env python3

import os


testfile = "../tests/13.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/13.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]


def part1(timetable):
    earliest = int(timetable[0])
    busses = [int(x) for x in timetable[1].split(',') if x != 'x']
    wait = earliest
    soonest = None
    for b in busses:
        nextBus = b - earliest%b
        if nextBus < wait:
            wait = nextBus
            soonest = b
    return soonest*wait


if __name__ == '__main__':
    print("Tests:")
    print("Part 1:", part1(testInput))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput))
