#! /usr/bin/env python3

import os


testfile = "../tests/04.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.replace('\n', ' ').strip() for x in f.read().split('\n\n')]

inputfile = "../input/04.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.replace('\n', ' ').strip() for x in f.read().split('\n\n')]


def validateDocument(doc):
    passport = dict([d.split(':') for d in doc.split(' ')])
    expectedFields = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        # "cid",
    ]
    return all([ef in passport.keys() for ef in expectedFields])


def part1(passports):
    validPassports = [validateDocument(p) for p in passports].count(True)
    return validPassports


if __name__ == '__main__':
    print("Tests:")
    print("Part 1:", part1(testInput))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput))
