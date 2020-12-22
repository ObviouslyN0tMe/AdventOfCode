import copy
import timeit

# puzzle input
with open("puzzle input") as file:
    rawdata = [x.strip(":\n") for x in file.readlines()]
# test input
with open("test input") as file:
    testdata = [x.strip(":\n") for x in file.readlines()]

round_count = 0


def formatData(data):
    formated_data = {}
    player = ""
    for line in data:
        if line.startswith("Player"):
            player = line
            formated_data[player] = []
        else:
            formated_data[player].append(int(line))
    return formated_data


def playCombat(player_decks):
    while True:
        # collect cards from top of decks
        played_cards = [player_decks["Player 1"].pop(0), player_decks["Player 2"].pop(0)]
        # determine round winner
        round_winner = "Player " + str(played_cards.index(max(played_cards)) + 1)
        # add cards to round winners deck in the right order
        if round_winner == "Player 2":
            played_cards.reverse()
        player_decks[round_winner] += played_cards
        # check if any player has no cards left
        if len(player_decks["Player 1"]) == 0 or len(player_decks["Player 2"]) == 0:
            return round_winner


def playRecursiveCombat(player_decks):
    played_rounds = []
    subgame_decks = {}
    while True:
        # endless games end with player 1 winning
        saved_decks = player_decks["Player 1"].copy() + [""] + player_decks["Player 2"].copy()
        if saved_decks in played_rounds:
            return "Player 1"
        else:
            played_rounds.append(saved_decks)
        # collect cards from top of decks
        played_cards = [player_decks["Player 1"].pop(0), player_decks["Player 2"].pop(0)]
        # determine round winner via subgame
        if played_cards[0] <= len(player_decks["Player 1"]) and played_cards[1] <= len(player_decks["Player 2"]):
            subgame_decks["Player 1"] = player_decks["Player 1"][:played_cards[0]].copy()
            subgame_decks["Player 2"] = player_decks["Player 2"][:played_cards[1]].copy()
            if max(subgame_decks["Player 1"]) > max(subgame_decks["Player 2"]):
                round_winner = "Player 1"
            else:
                round_winner = playRecursiveCombat(subgame_decks)
        # determine round winner via higher card
        else:
            round_winner = "Player " + str(played_cards.index(max(played_cards)) + 1)
        # add cards to round winners deck in the right order
        if round_winner == "Player 2":
            played_cards.reverse()
        player_decks[round_winner] += played_cards
        # check if any player has no cards left
        if len(player_decks["Player 1"]) == 0 or len(player_decks["Player 2"]) == 0:
            return round_winner


def countScore(deck):
    score = 0
    for multiplier, card in enumerate(reversed(deck), 1):
        score += card * multiplier
    return score


def setup():
    global decks
    new_decks = copy.deepcopy(decks)
    return new_decks


def run_part2():
    new_decks = setup()
    winner = playRecursiveCombat(new_decks)


decks = formatData(rawdata)
decks_part1 = copy.deepcopy(decks)
decks_part2 = copy.deepcopy(decks)
winner_part1 = playCombat(decks_part1)
winner_part2 = playRecursiveCombat(decks_part2)
print("Part 1:", countScore(decks_part1[winner_part1]))
print("Part 2:", countScore(decks_part2[winner_part2]))


setupcode = """
from __main__ import run_part2
"""

print(timeit.timeit(stmt="run_part2()", setup=setupcode, number=10))
