#! /usr/bin/env python3

import os


testfile = "../tests/22.txt"
with open( os.path.join(os.path.dirname(__file__), testfile) ) as f:
    testInput = f.read().strip()

inputfile = "../input/22.txt"
with open( os.path.join(os.path.dirname(__file__), inputfile) ) as f:
    myInput = f.read().strip()


class recursiveCombat():
    def __init__(self, players):
        self.players = players
        self.previousRounds = []

    def __repr__(self):
        return '|'.join([','.join([str(x) for x in p]) for p in self.players])

    def playGame(self):
        while all([len(p) for p in self.players]):
            # Tiebreaker
            thisRound = str(self)
            if thisRound in self.previousRounds:
                winner = 0
                break
            else:
                self.previousRounds.append(thisRound)

            # Regular play
            cardsDrawn = []
            for p in range(0, len(self.players)):
                cardsDrawn.append(self.players[p].pop(0))

            # Recursive combat
            if all([len(self.players[p]) >= cardsDrawn[p] for p in range(len(self.players))]):
                subDeck = [self.players[p][:cardsDrawn[p]] for p in range(len(self.players))]
                newGame = recursiveCombat(subDeck)
                winner = newGame.playGame()

            # Not enough cards, regular
            else:
                highest = -1
                winner = None
                for c in cardsDrawn:
                    if c >highest:
                        highest = c
                        winner = cardsDrawn.index(c)

            self.players[winner].append(cardsDrawn.pop(winner))
            self.players[winner].append(cardsDrawn.pop())

        return winner


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


def getWinnerScore(decks):
    cardCount = [len(p) for p in decks]
    winner = cardCount.index(max(cardCount))
    winnersScore = 0
    multiplier = len(decks[winner])
    for c in range(0, len(decks[winner])):
        winnersScore += multiplier*decks[winner][c]
        multiplier -= 1
    return winnersScore


def part1(cardDecks):
    players = cardDecks.split('\n\n')
    for p in range(0, len(players)):
        players[p] = [int(x) for x in players[p].split('\n')[1:]]

    while all([len(p) for p in players]):
        playRound(players)

    return getWinnerScore(players)


def part2(cardDecks):
    players = cardDecks.split('\n\n')
    for p in range(0, len(players)):
        players[p] = [int(x) for x in players[p].split('\n')[1:]]
    game = recursiveCombat(players)
    game.playGame()

    return getWinnerScore(game.players)


if __name__ == '__main__':
    print("Tests:")
    print("Part 1:", part1(testInput))
    print("Part 2:", part2(testInput))

    print()

    print("Mine:")
    print("Part 1:", part1(myInput))
    print("Part 2:", part2(myInput))
