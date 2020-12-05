#! /usr/bin/env python3

import os


testfile = "../tests/05.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/05.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]


def getSeatNumber(boardingPass):
    for r in ['F0', 'B1', 'L0', 'R1']:
        boardingPass = boardingPass.replace(r[0], r[1])
    row = int(boardingPass[:7], 2)
    col = int(boardingPass[7:], 2)
    return row*8 + col


def part1(boardingPasses):
    seatNumbers = [getSeatNumber(p) for p in boardingPasses]
    return max(seatNumbers)


if __name__ == '__main__':
    print("Tests:")
    print("Part 1:", part1(testInput))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput))
