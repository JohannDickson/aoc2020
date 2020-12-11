#! /usr/bin/env python3

import os
from helper import printGrid
from copy import deepcopy


testfile = "../tests/11.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [list(x.strip()) for x in f.readlines()]

inputfile = "../input/11.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [list(x.strip()) for x in f.readlines()]


def emptyNeighbours(seat, s):
    (y,x) = seat
    try:
        neighbours = [
            s[y-1][x-1],
            s[y-1][x],
            s[y-1][x+1],
            s[y][x-1],
            s[y][x+1],
            s[y+1][x-1],
            s[y+1][x],
            s[y+1][x+1]
        ]
        return all([n in ['L', '.'] for n in neighbours])
    except IndexError:
        print('WAT', (y,x))
        printGrid(s, False)
        raise


def busyNeighbours(seat, s):
    (y,x) = seat
    try:
        neighbours = [
            s[y-1][x-1],
            s[y-1][x],
            s[y-1][x+1],
            s[y][x-1],
            s[y][x+1],
            s[y+1][x-1],
            s[y+1][x],
            s[y+1][x+1]
        ]
        return (neighbours.count('#')>=4)
    except IndexError:
        print('WAT', (y,x))
        printGrid(s, False)
        raise


def calculateSeats(seating):
    newSeats = deepcopy(seating)

    for y in range(1, len(seating)-1):
        for x in range(1, len(seating[y])-1):
            if seating[y][x] == 'L' and emptyNeighbours((y,x), seating):
                newSeats[y][x] = '#'
            elif seating[y][x] == '#'and busyNeighbours((y,x), seating):
                newSeats[y][x] = 'L'

    return newSeats


def part1(seating):
    oldSeats = ''
    iterations = 0

    # Padding
    seating.insert(0, ['.']*len(seating[0]))
    seating.append(['.']*len(seating[0]))
    for i in range(0, len(seating)):
        seating[i].insert(0, '.')
        seating[i].append('.')

    while printGrid(seating, False) != oldSeats:
        oldSeats = printGrid(seating, False)
        seating = calculateSeats(seating)
        iterations+=1
        printGrid(seating, True)

    return printGrid(seating, False).count('#')


if __name__ == '__main__':
    print("Tests:")
    print("Part 1:", part1(testInput))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput))
