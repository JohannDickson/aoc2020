#! /usr/bin/env python3

import os
from copy import deepcopy
from time import sleep


testInput = "../tests/03.txt"
with open( os.path.join(os.path.dirname(__file__), testInput) ) as f:
    testInput = [list(x.strip()) for x in f.readlines()]


def printGrid(gridToPrint):
    for y in gridToPrint:
        print(''.join(y))


def part1(treeGrid, slope_x, slope_y):
    originalGrid = deepcopy(treeGrid)
    my_pos = [0,0]
    treeCounter = 0


    grid_width = len(treeGrid[0])
    grid_height = len(treeGrid)

    # Initial increment, all others at end of loop
    my_pos[0] += slope_y
    my_pos[1] += slope_x
    printGrid(treeGrid)

    while my_pos[0] < grid_height:

        while my_pos[1] >= len(treeGrid[my_pos[0]]):
            treeGrid[my_pos[0]].extend(originalGrid[my_pos[0]])

        if treeGrid[my_pos[0]][my_pos[1]] == '#':
            treeCounter += 1
            treeGrid[my_pos[0]][my_pos[1]] = 'X'
        else:
            treeGrid[my_pos[0]][my_pos[1]] = 'O'

        my_pos[0] += slope_y
        my_pos[1] += slope_x

        os.system('clear')
        printGrid(treeGrid)
        sleep(0.4)

    return treeCounter


if __name__ == '__main__':
    print("Tests:")
    print("Part 1:", part1(testInput, 3, 1))

