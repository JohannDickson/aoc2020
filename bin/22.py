#! /usr/bin/env python3

import os


testfile = "../tests/22.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = f.read().strip()

inputfile = "../input/22.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = f.read().strip()


def playRound(players):
    cardsDrawn = []
    for p in range(0, len(players)):
        cardsDrawn.append(players[p].pop(0))
    highest = -1
    winner = None
    for c in cardsDrawn:
        if c > highest:
            highest = c
            winner = cardsDrawn.index(c)
    players[winner].extend(sorted(cardsDrawn, reverse=True))
    return players


def part1(cardDecks):
    players = cardDecks.split('\n\n')
    for p in range(0, len(players)):
        players[p] = [int(x) for x in players[p].split('\n')[1:]]

    while all([len(p) for p in players]):
        playRound(players)

    cardCount = [len(p) for p in players]
    winner = cardCount.index(max(cardCount))
    winnersScore = 0
    multiplier = len(players[winner])
    for c in range(0, len(players[winner])):
        winnersScore += multiplier*players[winner][c]
        multiplier -= 1

    return winnersScore


if __name__ == '__main__':
    print("Tests:")
    print("Part 1:", part1(testInput))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput))
