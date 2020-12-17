#! /usr/bin/env python3

import os
from helper import printGrid, addPadding
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


    def __init__(self, x, y, z, active, addNeighbours=True):
        self.x = x
        self.y = y
        self.z = z
        self.active = active
        self.pending = None
        self.neighbours = []

        if x not in self.allCubeDict:
            self.allCubeDict[x] = {}
        if y not in self.allCubeDict[x]:
            self.allCubeDict[x][y] = {}
        self.allCubeDict[x][y][z] = self

        for ix in [-1,0,1]:
            for iy in [-1,0,1]:
                for iz in [-1,0,1]:
                    nx = self.x+ix
                    ny = self.y+iy
                    nz = self.z+iz
                    if nx!=x and ny!=y and nz!=z:
                        self.neighbours.append((nx, ny, nz))

        if addNeighbours:
            self.addNeighbours()

    def addNeighbours(self):
        for n in self.neighbours:
            nx,ny,nz = n
            if nx not in self.allCubeDict:
                self.allCubeDict[nx] = {}
            if ny not in self.allCubeDict[nx]:
                self.allCubeDict[nx][ny] = {}

            if nz not in self.allCubeDict[nx][ny].keys():
                cube(nx,ny,nz, False, addNeighbours=False)

    def countActiveNeighbours(self):
        activeCounter = 0
        for n in self.neighbours:
            nx,ny,nz = n
            if nx in cube.allCubeDict.keys():
                if ny in cube.allCubeDict[nx].keys():
                    if nz in cube.allCubeDict[nx][ny].keys():
                        if cube.allCubeDict[nx][ny][nz].active:
                            activeCounter+=1
        return activeCounter

    def countActive():
        activeCounter = 0
        for x in cube.allCubeDict.keys():
            for y in cube.allCubeDict[x].keys():
                for z in cube.allCubeDict[x][y].keys():
                    c = cube.allCubeDict[x][y][z]
                    if c.active:
                        activeCounter+=1
        return activeCounter

    def updateActive():
        for x in cube.allCubeDict.keys():
            for y in cube.allCubeDict[x].keys():
                for z in cube.allCubeDict[x][y].keys():
                    c = cube.allCubeDict[x][y][z]
                    activeNeighbours = c.countActiveNeighbours()
                    if c.active:
                        if not (2 <= activeNeighbours <= 3):
                            # print(x,y,z, c.active, 'NOW INACTIVE')
                            c.pending = False
                    elif activeNeighbours == 3:
                            print(x,y,z, c.active, 'WAKING UP')
                            c.pending = True
                            c.addNeighbours()
                    else:
                        # print(x,y,z, c.active, 'NO CHANGE')
                        pass


        for x in cube.allCubeDict.keys():
            for y in cube.allCubeDict[x].keys():
                for z in cube.allCubeDict[x][y].keys():
                    c = cube.allCubeDict[x][y][z]
                    if c.pending is not None:
                        c.active = c.pending
                        c.pending = None





def part1(cubeSlice, iterations):
    # pprint(cubeSlice, indent=4, compact=False)

    for y in range(0, len(cubeSlice)):
        for x in range(0, len(cubeSlice[y])):
            active = False
            if cubeSlice[y][x] == '#':
                active = True
            cube(x, y, 0, active)

    # print(cube.countActive())
    # pprint(cube.allCubeDict, indent=4, compact=False)
    for i in range(0,6):
        cube.updateActive()
        print('ITERATION', i)
        print('ACTIVE', cube.countActive())
        # pprint(cube.allCubeDict, indent=4, compact=False)


    return cube.countActive()

if __name__ == '__main__':
    print("Tests:")
    print("Part 1:", part1(testInput, 6), 112)

    print()

    print("Mine:")
    # print("Part 1:", part1(myInput, 6))
