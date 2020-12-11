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
