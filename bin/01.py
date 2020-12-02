#! /usr/bin/env python3

import os

inputfile = "../tests/01.txt"

with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    numbers = [int(x) for x in f.readlines()]


def part1(numbers):
    for i in range(0, len(numbers)):
        n = numbers[i]
        for j in range(0, len(numbers[i:])):
            m = numbers[i+j]
            if (n+m) == 2020:
                return n*m


def part2(numbers):
    for i in range(0, len(numbers)):
        n = numbers[i]
        for j in range(0, len(numbers[i:])):
            m = numbers[i+j]
            for k in range(0, len(numbers[i+j:])):
                o = numbers[i+j+k]
                if (n+m+o) == 2020:
                    return n*m*o


if __name__ == '__main__':
    print("Part 1:", part1(numbers))
    print("Part 2:", part2(numbers))
