#! /usr/bin/env python3

import os
import re


testfile = "../tests/14.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/14.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]


def part1(initialization):
    memAddresses = []
    remem = re.compile('^mem\[(\d+)\] = (\d+)')
    remask = re.compile('^mask = ([01X]+)')
    currentMask = ''
    memory = [0]

    for x in initialization:
        mask = remask.match(x)
        mem = remem.match(x)
        if mask:
            currentMask = list(mask[1])
        elif mem:
            address = int(mem[1])
            value = int(mem[2])
            if address > len(memory):
                memory.extend([0]*(address - len(memAddresses)))

            bval = list(format(value, '036b'))
            for i in range(0, len(currentMask)):
                if currentMask[i] != 'X':
                    bval[i] = currentMask[i]

            memory[address] = int(''.join(bval), 2)

    return sum(memory)


if __name__ == '__main__':
    print("Tests:")
    print("Part 1:", part1(testInput))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput))
