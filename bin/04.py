#! /usr/bin/env python3

import os


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
    if  1920 <= int(p['byr']) <= 2002:
        pass
    else:
        print("INVALID byr", p['byr'])
        return False

    if 2010 <= int(p['iyr']) <= 2020:
        pass
    else:
        print("INVALID iyr", p['iyr'])
        return False

    if 2020 <= int(p['eyr']) <= 2030:
        pass
    else:
        print("INVALID eyr", p['eyr'])
        return False

    if (p['hgt'][-2:] == 'cm' and 150 <= int(p['hgt'][:-2]) <= 193) \
    or p['hgt'][-2:] == 'in' and 59 <= int(p['hgt'][:-2]) <= 76:
        pass
    else:
        print("INVALID hgt", p['hgt'])
        return False

    if p['hcl'][0] == '#' and len(p['hcl']) == 7:
        pass
    else:
        print("INVALID hcl", p['hcl'])
        return False

    if p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        pass
    else:
        print("INVALID ecl", p['ecl'])
        return False

    if p['pid']:
        pass
    else:
        print("INVALID pid", p['pid'])
        return False

    print('VALID')
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
