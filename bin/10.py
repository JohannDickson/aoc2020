#! /usr/bin/env python3

import os


# testfile = "../tests/10_1_1.txt"
testfile = "../tests/10_1_2.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [int(x.strip()) for x in f.readlines()]

inputfile = "../input/10.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [int(x.strip()) for x in f.readlines()]


def part1(adapters):
    maxRating = max(adapters)+3
    seatSocket = 0
    adapters = sorted([seatSocket]+adapters+[maxRating])
    joltDiffs = {1:0, 2:0, 3:0}

    for i in range(1, len(adapters)):
        joltDiffs[adapters[i] - adapters[i-1]] += 1

    return joltDiffs[1]*joltDiffs[3]


def findPermutations(adapters):
    global pCounter
    permutation = [adapters[0]]

    if len(adapters) == 2:
        pCounter += 1

    for j in [1,2,3]:
        try:
            if adapters[j] - adapters[0] <= 3:
                permutation.append(findPermutations(adapters[j:]))
        except IndexError:
            pass

    return permutation


def countPermutations(permutations):
    global pCounter

    l = len(permutations)
    if l > 2:
        [countPermutations(x) for x in permutations[1:]]
    if l == 2:
        countPermutations(permutations[1])
    elif len(permutations) == 1:
        pCounter += 1


def part2(adapters):
    global pCounter

    maxRating = max(adapters)+3
    seatSocket = 0
    adapters = sorted([seatSocket]+adapters+[maxRating])

    pCounter = 0
    allPermutations = findPermutations(adapters)
    return pCounter


if __name__ == '__main__':
    print("Tests:")
    print("Part 1:", part1(testInput))
    print("Part 2:", part2(testInput))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput))
