#! /usr/bin/env python3

import os


testfile = "../tests/15.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [int(x) for x in f.read().strip().split(',')]

inputfile = "../input/15.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [int(x) for x in f.read().strip().split(',')]


def part1(numbers, turns):
    memory = {n: {'lastTurn': numbers.index(n)+1, 'count': 1} for n in numbers}

    last = numbers[-1]
    for i in range(len(numbers)+1, turns+1):

        if memory[last]['count'] == 1:
            memory[0]['difference'] = i - memory[0]['lastTurn']
            memory[0]['lastTurn'] = i
            memory[0]['count'] += 1
            last = 0

        else:
            last = memory[last]['difference']
            if last in memory.keys():
                memory[last]['difference'] = i - memory[last]['lastTurn']
                memory[last]['lastTurn'] = i
                memory[last]['count'] += 1
            else:
                memory[last] = {
                    'count': 1,
                    'lastTurn': i,
                    'difference': 0,
                }

    return last


if __name__ == '__main__':
    print("Tests:")
    print("Part 1:", part1(testInput, 10))
    print("Part 2:", part1(testInput, 30000000))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput, 2020))
    print("Part 2:", part1(myInput, 30000000))
