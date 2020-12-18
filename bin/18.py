#! /usr/bin/env python3

import os
import re


testfile = "../tests/18_2.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/18.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]


def solve(equation, plusPrecedence=False):
    p = re.compile('(\([^\(\)]*?\))')
    subEquations = p.findall(equation)
    while subEquations:
        newEq = subEquations[0]
        newSol = solve(newEq[1:-1], plusPrecedence)
        equation = equation.replace(newEq, newSol)
        subEquations = p.findall(equation)
    operators = equation.split(' ')

    while plusPrecedence and operators.count('+') > 0:
        left = operators[operators.index('+')-1]
        right = operators[operators.index('+')+1]
        result = str(int(left)+int(right))
        operators = operators[:operators.index('+')-1]+[result]+operators[operators.index('+')+2:]

    result = operators.pop(0)
    for i in range(0, len(operators), 2):
        op, num = operators[i], operators[i+1]
        newEq = ' '.join([result, op, num])
        result = str(eval(newEq))
    return result


def part1(maths, plusPrecedence=False):
    solutions = []
    for e in maths:
        solutions.append(solve(e, plusPrecedence))
    return sum([int(x) for x in solutions])

if __name__ == '__main__':
    print("Tests:")
    # print("Part 1:", part1(testInput))
    print("Part 2:", part1(testInput, True))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput))
    print("Part 2:", part1(myInput, True))
