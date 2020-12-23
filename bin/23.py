#! /usr/bin/env python3

import os
from collections import deque


testfile = "../tests/23.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [int(x) for x in f.read().strip()]

inputfile = "../input/23.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [int(x) for x in f.read().strip()]


def part1(cups, turns):
    cups = deque(cups)

    for i in range(0, turns):
        pending = []
        current = cups[0]
        cups.rotate(-1)
        for _ in range(3):
            pending.append(cups.popleft())
        target = current-1
        while target in pending:
            target-=1

        if target < min(cups):
            target=max(cups)

        cups.rotate(-(cups.index(target)+1))
        cups.extend(pending)
        cups.rotate(-(cups.index(current)+1))

    cups.rotate(- (cups.index(1)))
    return ''.join([str(c) for c in list(cups)][1:])


if __name__ == '__main__':
    print("Tests:")
    print("Part 1:", part1(testInput, 10))
    print("Part 1:", part1(testInput, 100))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput, 100))
