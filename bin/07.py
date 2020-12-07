#! /usr/bin/env python3

import os
import re


# testfile = "../tests/07.txt"
testfile = "../tests/07_2.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/07.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]


def getBagContents(bag):
    currentBag, contents = bag.split(' bags contain ')

    noBag = re.compile("no other bags\.$")
    bagFilter = re.compile("((\d+) ([a-z ]+) bag)")

    if noBag.match(contents):
        return {currentBag: ''}

    whatsInTheBag = {}
    for b in bagFilter.findall(contents):
        whatsInTheBag[b[2]] = b[1]
    return {currentBag: whatsInTheBag}


def findParents(bag, allbags):
    parents = set([])
    for b in allbags:
        if bag in allbags[b]:
            parents.update([b])
            parents.update(findParents(b, allbags))
    return parents

def findChildren(bag, allbags):
    childBags = 0
    for c in allbags[bag]:
        qt = allbags[bag][c]
        for i in range(0, int(qt)):
            childBags += 1
            childBags += findChildren(c, allbags)
    return childBags


def part1(bags):
    allBags = {}
    for bag in bags:
        allBags.update(getBagContents(bag))
    return len(findParents('shiny gold', allBags))


def part2(bags):
    allBags = {}
    for bag in bags:
        allBags.update(getBagContents(bag))
    return findChildren('shiny gold', allBags)


if __name__ == '__main__':
    print("Tests:")
    print("Part 1:", part1(testInput))
    print("Part 2:", part2(testInput))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput))
    print("Part 2:", part2(myInput))
