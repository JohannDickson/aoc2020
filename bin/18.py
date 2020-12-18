#! /usr/bin/env python3

import os
import re


testfile = "../tests/18_1.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/18.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]


def solve(equation):
    print(equation)
    p = re.compile('(\([^\(\)]*?\))')
    subEquations = p.findall(equation)
    while subEquations:
        newEq = subEquations[0]
        newSol = solve(newEq[1:-1])
        equation = equation.replace(newEq, newSol)
        subEquations = p.findall(equation)
    operators = equation.split(' ')
    result = operators.pop(0)
    for i in range(0, len(operators), 2):
        op, num = operators[i], operators[i+1]
        newEq = ' '.join([result, op, num])
        result = str(eval(newEq))
    return result


def part1(maths):
    solutions = []
    for e in maths:
        solutions.append(solve(e))
    return sum([int(x) for x in solutions])


if __name__ == '__main__':
    print("Tests:")
    print("Part 1:", part1(testInput))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput))
