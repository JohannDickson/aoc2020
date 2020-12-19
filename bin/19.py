#! /usr/bin/env python3

import os
import re
from copy import deepcopy


testfile = "../tests/19_2.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = f.read().strip()

inputfile = "../input/19.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = f.read().strip()


def part1(imageData):
    messageRules, receivedMessages = imageData.split('\n\n')
    rules = {}
    letters = {}

    for entry in messageRules.split('\n'):
        e,n = entry.split(': ')
        if '"' in n:
            rules[e] = n[1:-1]
            letters[e] = n[1:-1]
        else:
            rules[e] = n.split()

    solved = {e:False for e in rules.keys()}
    for l in letters:
        solved[l] = True

    regregex = re.compile('[\(\)\|\+'+''.join(letters.values())+']')

    while not all(solved.values()):
        for k in [x for x in solved.keys() if not solved[x]]:
            for j in range(0, len(rules[k])):

                if rules[k][j] == k:
                    if k == '8':
                        rules[k][j] = '+'
                    if k == '11':
                        pass

                for l in letters:
                    if rules[k][j] == l:
                        rules[k][j] = letters[l]
                        break

                    for a in [x for x in solved.keys() if solved[x]]:
                        if rules[k][j] == a:
                            rules[k][j] = rules[a]
                            break

                if (all([regregex.match(x) for x in rules[k]])):
                    rules[k] = '('+''.join(rules[k])+')'
                    solved[k] = True

    validMessages = []
    stringCheck = re.compile('^'+rules['0']+'$')
    for m in receivedMessages.split('\n'):
        if stringCheck.match(m):
            validMessages.append(m)

    return len(validMessages)


def part2(imageData):
    imageData = imageData.replace("8: 42\n", "8: 42 | 42 8\n")
    imageData = imageData.replace("11: 42 31\n", "11: 42 31 | 42 11 31\n")
    return part1(imageData)


if __name__ == '__main__':
    print("Tests:")
    print("Part 1:", part1(testInput))
    print("Part 2:", part2(testInput))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput))
    print("Part 2:", part2(myInput))
