#! /usr/bin/env python3

import os
from copy import deepcopy
from time import sleep


testfile = "../tests/03.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [list(x.strip()) for x in f.readlines()]


def printGrid(gridToPrint, display):
    if display:
        out = '\n'.join([''.join(y) for y in gridToPrint])
        os.system('clear')
        print(out)
        sleep(0.2)


def part1(treeGrid, slope_x, slope_y, display=False):
    myGrid = deepcopy(treeGrid)
    posX = 0
    posY = 0
    treeCounter = 0

    grid_width = len(treeGrid[0])
    grid_height = len(treeGrid)

    printGrid(treeGrid, display)

    while posY < grid_height:

        while posX >= len(myGrid[posY]):
            myGrid[posY].extend(treeGrid[posY])

        if myGrid[posY][posX] == '#':
            treeCounter += 1
            myGrid[posY][posX] = 'X'
        else:
            myGrid[posY][posX] = 'O'

        posY += slope_y
        posX += slope_x

        printGrid(myGrid, display)

    return treeCounter


def part2(treeGrid, slopes, display=False):
    results = []
    for slope in slopes:
        results.append(part1(treeGrid, slope[0], slope[1], display))

    result = 1
    for i in results:
        result = result * i
    return result


if __name__ == '__main__':
    p1 = part1(testInput, 3, 1)
    p2 = part2(testInput, [(1,1), (3,1), (5,1), (7,1), (1,2)])
    print("Tests:")
    print("Part 1:", p1)
    print("Part 2:", p2)
