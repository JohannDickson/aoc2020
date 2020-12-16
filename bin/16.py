#! /usr/bin/env python3

import os
import re


testfile = "../tests/16_2.txt"
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


def part2(input):
    sections = input.split('\n\n')
    srules = sections[0].split('\n')
    smine = sections[1].split('\n')[1].split(',')
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
        matches = {f: [] for f in range(len(fields))}
        for f in range(len(fields)):
            for r in rules:
                if r['llb'] <= fields[f] <= r['lub'] or  r['ulb'] <= fields[f] <= r['uub']:
                    matches[f].append(r['name'])
        if all([f != [] for f in matches.values()]):
            tickets.append(matches)

    ticketFields = [r['name'] for r in rules]
    fieldOrdering = [None]*len(smine)
    foundFields = []
    while len(ticketFields):
        hasField={f:[] for f in ticketFields}
        for i in range(len(smine)):
            if i in foundFields:
                continue
            for f in ticketFields:
                if all([f in t[i] for t in tickets]):
                    hasField[f].append(i)
        fieldCount = {len(hasField[f]):f for f in hasField}
        fieldOrdering[hasField[fieldCount[1]][0]] = fieldCount[1]
        foundFields.append(hasField[fieldCount[1]][0])
        ticketFields.remove(fieldCount[1])

    valueMult = 1
    for i in range(len(fieldOrdering)):
        if fieldOrdering[i].startswith('departure'):
            valueMult *= int(smine[i])

    return valueMult


if __name__ == '__main__':
    print("Tests:")
    # print("Part 1:", part1(testInput))
    print("Part 2:", part2(testInput))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput))
    print("Part 2:", part2(myInput))
