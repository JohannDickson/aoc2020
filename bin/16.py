#! /usr/bin/env python3

import os
import re


testfile = "../tests/16.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = f.read().strip()

inputfile = "../input/16.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = f.read().strip()


def part1(input):
    sections = input.split('\n\n')
    srules = sections[0].split('\n')
    smine = sections[1].split('\n')[1]
    snearby = sections[2].split('\n')[1:]

    rules = []
    rule = re.compile('^([a-z ]+): (\d+)\-(\d+) or (\d+)\-(\d+)$')
    for r in srules:
        m = rule.match(r)
        rules.append({
            'name': m[1],
            'llb': int(m[2]),
            'lub': int(m[3]),
            'ulb': int(m[4]),
            'uub': int(m[5]),
            })

    tickets = []
    for n in snearby:
        fields = [int(x) for x in n.split(',')]
        matches = {f: [] for f in fields}
        for f in fields:
            for r in rules:
                if r['llb'] <= f <= r['lub'] or  r['ulb'] <= f <= r['uub']:
                    matches[f].append(r['name'])
        tickets.append(matches)

    invalidSum = 0
    for t in tickets:
        for k in t.keys():
            if t[k] == []:
                invalidSum += k

    return invalidSum


if __name__ == '__main__':
    print("Tests:")
    print("Part 1:", part1(testInput))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput))
