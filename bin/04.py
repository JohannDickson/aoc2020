#! /usr/bin/env python3

import os
import re


# testfile = "../tests/04.txt"
testfile = "../tests/04_2_1.txt"
# testfile = "../tests/04_2_2.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.replace('\n', ' ').strip() for x in f.read().split('\n\n')]

inputfile = "../input/04.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.replace('\n', ' ').strip() for x in f.read().split('\n\n')]


def parsePassport(doc):
    return dict([d.split(':') for d in doc.split(' ')])


def validateKeys(passport):
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


def validateValues(p):
    yrs = re.compile('^\d{4}$')
    hgt = re.compile('(\d+)(cm|in)')
    hcl = re.compile('#[a-f0-9]')
    pid = re.compile('^\d{9}$')


    if not (yrs.match(p['byr']) and (1920 <= int(p['byr']) <= 2002)):
        return False

    if not (yrs.match(p['iyr']) and (2010 <= int(p['iyr']) <= 2020)):
        return False

    if not (yrs.match(p['eyr']) and (2020 <= int(p['eyr']) <= 2030)):
        return False

    rhgt = hgt.match(p['hgt'])
    if not (rhgt and \
        ((rhgt[2] == 'cm' and 150 <= int(rhgt[1]) <= 193) \
        or (rhgt[2] == 'in' and 59 <= int(rhgt[1]) <= 76)) \
    ):
        return False

    if not (hcl.match(p['hcl'])):
        return False

    if not (p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
        return False

    if not (pid.match(p['pid'])):
        return False

    return True


def part1(passports):
    passports = [parsePassport(p) for p in passports]
    validPassports = [validateKeys(p) for p in passports].count(True)
    return validPassports


def part2(passports):
    passports = [parsePassport(p) for p in passports]
    validPassports = 0
    for passport in passports:
        if validateKeys(passport) and validateValues(passport):
            validPassports += 1

    return validPassports


if __name__ == '__main__':
    print("Tests:")
    print("Part 1:", part1(testInput))
    print("Part 2:", part2(testInput))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput))
    print("Part 2:", part2(myInput))
