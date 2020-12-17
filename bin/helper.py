#! /usr/bin/env python3

import os
from time import sleep


def printGrid(gridToPrint, display):
    out = '\n'.join([''.join(y) for y in gridToPrint])
    if display:
        os.system('clear')
        print(out)
        sleep(0.2)
    return out


def printDictGrid(gridToPrint, display):
    out = ''
    for y in sorted(gridToPrint.keys()):
        for x in sorted(gridToPrint[y].keys()):
            out+=str(gridToPrint[y][x])
        out+='\n'
    if display:
        os.system('clear')
        print(out)
        sleep(0.2)
    return out


def addPadding(grid):
    grid.insert(0, ['.']*len(grid[0]))
    grid.append(['.']*len(grid[0]))
    for i in range(0, len(grid)):
        grid[i].insert(0, '.')
        grid[i].append('.')
    return grid
