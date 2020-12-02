#! /usr/bin/env python3

import os

inputfile = "../tests/02.txt"

with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    entries = [x.strip() for x in f.readlines()]

validPasswords = 0

for i in entries:
    limits, letter, password = i.split(" ")
    lower, upper = limits.split("-")
    letter = letter[:-1]

    if int(lower) <= password.count(letter) <= int(upper):
        validPasswords += 1

print("Part 1:", validPasswords)
