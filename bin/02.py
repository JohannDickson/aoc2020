#! /usr/bin/env python3

import os

inputfile = "../tests/02.txt"

with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    entries = [x.strip() for x in f.readlines()]


def part1(entries):
    validPasswords = 0

    for i in entries:
        limits, letter, password = i.split(" ")
        lower, upper = limits.split("-")
        letter = letter[:-1]

        if int(lower) <= password.count(letter) <= int(upper):
            validPasswords += 1

    return validPasswords


def part2(entries):
    validPasswords = 0

    for i in entries:
        limits, letter, password = i.split(" ")
        lower, upper = [int(x) for x in limits.split("-")]
        letter = letter[:-1]

        if (password[lower-1] == letter and password[upper-1] != letter) \
        or (password[lower-1] != letter and password[upper-1] == letter):
            validPasswords += 1

    return validPasswords


print("Part 1:", part1(entries))
print("Part 2:", part2(entries))