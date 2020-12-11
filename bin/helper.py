#! /usr/bin/env python3

import os
from time import sleep


def printGrid(gridToPrint, display):
    if display:
        out = '\n'.join([''.join(y) for y in gridToPrint])
        os.system('clear')
        print(out)
        sleep(0.2)
