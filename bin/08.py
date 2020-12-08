#! /usr/bin/env python3

import os


testfile = "../tests/08.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = [x.strip() for x in f.readlines()]

inputfile = "../input/08.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = [x.strip() for x in f.readlines()]


def processInstruction(ins, commands):
    global accumulator

    act, val = commands[ins].split()

    nextIns = ins+1
    if act == 'acc':
        accumulator += int(val)
    if act == 'jmp':
        nextIns = ins+int(val)
    if act == 'nop':
        pass

    return nextIns


def part1(instructionSet):
    global accumulator
    accumulator = 0
    previousInstructions = []

    instruction = 0
    while instruction not in previousInstructions:
        previousInstructions.append(instruction)
        instruction = processInstruction(instruction, instructionSet)

    return accumulator


if __name__ == '__main__':
    print("Tests:")
    print("Part 1:", part1(testInput))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput))
