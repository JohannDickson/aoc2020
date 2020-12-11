#! /usr/bin/env python3

import os
from helper import printGrid
from copy import deepcopy


# testfile = "../tests/11.txt"
testfile = "../tests/11_2.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [list(x.strip()) for x in f.readlines()]

inputfile = "../input/11.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [list(x.strip()) for x in f.readlines()]


def emptyNeighbours(neighbours):
    return all([n in ['L', '.'] for n in neighbours])


def busyNeighbours(neighbours, limit):
    return (neighbours.count('#')>=limit)


def calculateSeats(seating):
    newSeats = deepcopy(seating)

    for y in range(1, len(seating)-1):
        for x in range(1, len(seating[y])-1):
            neighbours = [
                seating[y-1][x-1],
                seating[y-1][x],
                seating[y-1][x+1],
                seating[y][x-1],
                seating[y][x+1],
                seating[y+1][x-1],
                seating[y+1][x],
                seating[y+1][x+1]
            ]
            if seating[y][x] == 'L' and emptyNeighbours(neighbours):
                newSeats[y][x] = '#'
            elif seating[y][x] == '#'and busyNeighbours(neighbours, 4):
                newSeats[y][x] = 'L'

    return newSeats


def calculateVisibleSeats(seating):
    newSeats = deepcopy(seating)

    seats = []
    for y in range(1, len(seating)-1):
        for x in range(1, len(seating[y])-1):
            ny, nx = y,x
            neighbours = []
            for c in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                ny, nx = y,x
                ny += c[0]
                nx += c[1]

                while (0 < ny < len(seating)) and (0 < nx < len(seating[0])):
                    try:
                        if seating[ny][nx] in ['L', '#']:
                            neighbours += seating[ny][nx]
                            break
                    except IndexError:
                        print('WAT', (y,x))
                        printGrid(s, False)
                        raise
                    ny += c[0]
                    nx += c[1]
                else:
                    neighbours.append('.')

            if seating[y][x] == 'L' and emptyNeighbours(neighbours):
                newSeats[y][x] = '#'
            elif seating[y][x] == '#'and busyNeighbours(neighbours, 5):
                newSeats[y][x] = 'L'

    return newSeats


def addPadding(grid):
    grid.insert(0, ['.']*len(grid[0]))
    grid.append(['.']*len(grid[0]))
    for i in range(0, len(grid)):
        grid[i].insert(0, '.')
        grid[i].append('.')
    return grid


def part1(seating):
    oldSeats = ''
    iterations = 0

    seating = addPadding(seating)

    while printGrid(seating, False) != oldSeats:
        oldSeats = printGrid(seating, False)
        seating = calculateSeats(seating)
        iterations+=1
        printGrid(seating, True)

    return printGrid(seating, False).count('#')


def part2(seating):
    oldSeats = ''
    iterations = 0

    seating = addPadding(seating)

    while printGrid(seating, False) != oldSeats:
        oldSeats = printGrid(seating, False)
        seating = calculateVisibleSeats(seating)
        iterations+=1
        printGrid(seating, True)

    return printGrid(seating, False).count('#')


if __name__ == '__main__':
    print("Tests:")
    # print("Part 1:", part1(testInput))
    print("Part 2:", part2(testInput))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput))
    print("Part 2:", part2(myInput))
