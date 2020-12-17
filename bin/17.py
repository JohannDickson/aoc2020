#! /usr/bin/env python3

import os
from copy import deepcopy
from helper import printDictGrid, addPadding
from pprint import pprint


testfile = "../tests/17.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [list(x.strip()) for x in f.readlines()]

inputfile = "../input/17.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [list(x.strip()) for x in f.readlines()]


class cube:
    allCubeDict={}

    def __repr__(self):
        if self.active:
            return '#'
        else:
            return '.'


    def __init__(self, x, y, z, w, active, addNeighbours=True):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.active = active
        self.pending = None
        self.neighbours = []

        if z not in cube.allCubeDict.keys():
            cube.allCubeDict[z] = {}
        if y not in cube.allCubeDict[z].keys():
            cube.allCubeDict[z][y] = {}
        if x not in cube.allCubeDict[z][y].keys():
            cube.allCubeDict[z][y][x] = {}
        cube.allCubeDict[z][y][x][w] = self

        for ix in [-1,0,1]:
            for iy in [-1,0,1]:
                for iz in [-1,0,1]:
                    for iw in [-1,0,1]:
                        nx = self.x+ix
                        ny = self.y+iy
                        nz = self.z+iz
                        nw = self.w+iw
                        if nx!=x or ny!=y or nz!=z or nw!=w:
                            self.neighbours.append((nx, ny, nz, nw))

        if addNeighbours:
            self.addNeighbours()

    def addNeighbours(self):
        for n in self.neighbours:
            nx,ny,nz, nw = n
            if nz not in cube.allCubeDict.keys():
                cube.allCubeDict[nz] = {}
            if ny not in cube.allCubeDict[nz].keys():
                cube.allCubeDict[nz][ny] = {}
            if nx not in cube.allCubeDict[nz][ny].keys():
                cube.allCubeDict[nz][ny][nx] = {}
            if nw not in cube.allCubeDict[nz][ny][nx].keys():
                cube(nx,ny,nz,nw, False, addNeighbours=False)

    def countActiveNeighbours(self):
        activeCounter = 0
        for n in self.neighbours:
            nx,ny,nz,nw = n
            if nz in cube.allCubeDict.keys():
                if ny in cube.allCubeDict[nz].keys():
                    if nx in cube.allCubeDict[nz][ny].keys():
                        if nw in cube.allCubeDict[nz][ny][nx].keys():
                            if cube.allCubeDict[nz][ny][nx][nw].active:
                                activeCounter+=1
        return activeCounter

    def countActive():
        activeCounter = 0
        for z in cube.allCubeDict.keys():
            for y in cube.allCubeDict[z].keys():
                for x in cube.allCubeDict[z][y].keys():
                    for w in cube.allCubeDict[z][y][x].keys():
                        c = cube.allCubeDict[z][y][x][w]
                        if c.active:
                            activeCounter+=1
        return activeCounter

    def updateActive():
        tempDict = deepcopy(cube.allCubeDict)
        for z in tempDict.keys():
            for y in tempDict[z].keys():
                for x in tempDict[z][y].keys():
                    for w in tempDict[z][y][x].keys():
                        c = cube.allCubeDict[z][y][x][w]
                        activeNeighbours = c.countActiveNeighbours()
                        if c.active and not (2 <= activeNeighbours <= 3):
                                c.pending = False
                        elif c.active == False and activeNeighbours == 3:
                                c.pending = True
                                c.addNeighbours()

        for z in cube.allCubeDict.keys():
            for y in cube.allCubeDict[z].keys():
                for x in cube.allCubeDict[z][y].keys():
                    for w in cube.allCubeDict[z][y][x].keys():
                        c = cube.allCubeDict[z][y][x][w]
                        if c.pending is not None:
                            c.active = c.pending
                            c.pending = None


def part2(cubeSlice, iterations):
    # pprint(cubeSlice, indent=4, compact=False)

    for y in range(0, len(cubeSlice)):
        for x in range(0, len(cubeSlice[y])):
            active = False
            if cubeSlice[y][x] == '#':
                active = True
            cube(x, y, 0, 0, active)

    # print(printDictGrid(cube.allCubeDict[0], False))
    for i in range(0,6):
        cube.updateActive()
        print('ITERATION', i)
        print('ACTIVE', cube.countActive())
        # print(printDictGrid(cube.allCubeDict[0], False))


    return cube.countActive()

if __name__ == '__main__':
    print("Tests:")
    # print("Part 2:", part2(testInput, 6), 848)

    print()

    print("Mine:")
    print("Part 2:", part2(myInput, 6))
