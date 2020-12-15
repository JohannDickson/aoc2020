#! /usr/bin/env python3

import os


testfile = "../tests/12.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/12.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]


class Ferry:
    def __init__(self, posX=0, posY=0):
        self.posX = posX
        self.posY = posY
        self.heading = 'E'
        self.degrees = 90
        self.wayX = waypoint[0]
        self.wayY = waypoint[1]

    def processInstruction(self, instruction):
        action = instruction[0]
        units = int(instruction[1:])

        if action == 'N' or (self.heading == 'N' and action == 'F'):
            self.posY += units
        elif action == 'S' or (self.heading == 'S' and action == 'F'):
            self.posY -= units
        elif action == 'E' or (self.heading == 'E' and action == 'F'):
            self.posX += units
        elif action == 'W' or (self.heading == 'W' and action == 'F'):
            self.posX -= units

        elif action == 'L':
            self.degrees -= units
            self.updateHeading(self.degrees)
        elif action == 'R':
            self.degrees += units
            self.updateHeading(self.degrees)

    def updateHeading(self, rotation):
        pointing = rotation%360
        self.degrees = rotation
        if pointing == 0:
            self.heading = 'N'
        elif pointing == 90:
            self.heading = 'E'
        elif pointing == 180:
            self.heading = 'S'
        elif pointing == 270:
            self.heading = 'W'

    def processWaypoint(self, instruction):
        action = instruction[0]
        units = int(instruction[1:])

        if action == 'N':
            self.wayY += units
        elif action == 'S':
            self.wayY -= units
        elif action == 'E':
            self.wayX += units
        elif action == 'W':
            self.wayX -= units

        elif action == 'L':
            self.degrees -= units
            self.updateHeading(self.degrees)
            for _ in range(units//90):
                ox, oy = self.wayX, self.wayY
                self.wayX = -oy
                self.wayY = ox
        elif action == 'R':
            self.degrees += units
            self.updateHeading(self.degrees)
            for _ in range(units//90):
                ox, oy = self.wayX, self.wayY
                self.wayX = oy
                self.wayY = -ox

        elif action == 'F':
            self.posY += units*self.wayY
            self.posX += units*self.wayX


def part1(navigation):
    myFerry = Ferry()
    for instruction in navigation:
        myFerry.processInstruction(instruction)
    return abs(myFerry.posX)+abs(myFerry.posY)


def part2(navigation):
    myFerry = Ferry(waypoint=(10, 1))
    for instruction in navigation:
        myFerry.processWaypoint(instruction)
    return abs(myFerry.posX)+abs(myFerry.posY)


if __name__ == '__main__':
    print("Tests:")
    print("Part 1:", part1(testInput))
    print("Part 2:", part2(testInput))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput))
    print("Part 2:", part2(myInput))
