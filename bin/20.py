#! /usr/bin/env python3

import os
import re


testfile = "../tests/20.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = f.read().strip()

inputfile = "../input/20.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = f.read().strip()


def part1(inputData):
    tiles = {}
    r = re.compile('Tile (\d+):')
    for t in inputData.split('\n\n'):
        t = t.split('\n')
        ref = r.match(t[0])[1]
        data = [list(l) for l in t[1:]]
        edges = [data[0], data[-1], [x[0] for x in data], [x[-1] for x in data]]
        edges.extend([list(reversed(e)) for e in edges])

        for i in range(0, len(edges)):
            edges[i] = ''.join(edges[i])

        tiles[ref] = {
            'reference': int(ref),
            'data': data,
            'edges': set(edges),
            'neighbours': set([])
        }

    for t in tiles.keys():
        for o in tiles.keys():
            if t == o: continue
            if tiles[t]['edges'] & tiles[o]['edges']:
                tiles[t]['neighbours'].add(o)
                tiles[o]['neighbours'].add(t)

    corners = []
    for t in tiles:
        if len(tiles[t]['neighbours']) == 2:
            corners.append(tiles[t]['reference'])

    result = 1
    for c in corners:
        result*=c
    return result


if __name__ == '__main__':
    print("Tests:")
    print("Part 1:", part1(testInput))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput))
