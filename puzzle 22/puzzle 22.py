import copy
import timeit


def playCombat(player_decks):
    while True:
        # collect cards from top of decks
        played_cards = [player_decks[0].pop(0), player_decks[1].pop(0)]
        # determine round winner
        round_winner = played_cards.index(max(played_cards))
        # add cards to round winners deck in the right order
        if round_winner == 1:
            played_cards.reverse()
        player_decks[round_winner] += played_cards
        # check if any player has no cards left
        if not player_decks[0] or not player_decks[1]:
            return round_winner


def playRecursiveCombat(player_decks):
    played_rounds = set()
    while True:
        # endless games end with player 1 winning
        saved_decks = (tuple(player_decks[0]), tuple(player_decks[1]))
        if saved_decks in played_rounds:
            return 0
        played_rounds.add(saved_decks)
        # collect cards from top of decks
        player1_card, player2_card = player_decks[0].pop(0), player_decks[1].pop(0)
        # determine round winner via higher card
        if player1_card > len(player_decks[0]) or player2_card > len(player_decks[1]):
            round_winner = player2_card > player1_card
        # determine round winner via subgame
        else:
            subgame_decks = [player_decks[0][:player1_card], player_decks[1][:player2_card]]
            if max(subgame_decks[0]) > max(subgame_decks[1]):
                round_winner = 0
            else:
                round_winner = playRecursiveCombat(subgame_decks)
        # add cards to round winners deck in the right order
        if round_winner:
            player_decks[round_winner] += [player2_card, player1_card]
        else:
            player_decks[round_winner] += [player1_card, player2_card]
        # check if any player has no cards left
        if not player_decks[1] or not player_decks[0]:
            return round_winner


def countScore(deck):
    score = 0
    for multiplier, card in enumerate(reversed(deck), 1):
        score += card * multiplier
    return score


def run():
    x = [[26, 8, 2, 17, 19, 29, 41, 7, 25, 33, 50, 16, 36, 37, 32, 4, 46, 12, 21, 48, 11, 6, 13, 23, 9],
         [27, 47, 15, 45, 10, 14, 3, 44, 31, 39, 42, 5, 49, 24, 22, 20, 30, 1, 35, 38, 18, 43, 28, 40, 34]]
    y = playRecursiveCombat(x)


decks = [[26, 8, 2, 17, 19, 29, 41, 7, 25, 33, 50, 16, 36, 37, 32, 4, 46, 12, 21, 48, 11, 6, 13, 23, 9],
         [27, 47, 15, 45, 10, 14, 3, 44, 31, 39, 42, 5, 49, 24, 22, 20, 30, 1, 35, 38, 18, 43, 28, 40, 34]]

decks_part1 = copy.deepcopy(decks)
decks_part2 = copy.deepcopy(decks)
winner_part1 = playCombat(decks_part1)
winner_part2 = playRecursiveCombat(decks_part2)
print("Part 1:", countScore(decks_part1[winner_part1]))
print("Part 2:", countScore(decks_part2[winner_part2]))

setupcode = """
from __main__ import run
from __main__ import decks
"""
print(timeit.timeit(stmt=run, setup=setupcode, number=500)/500)
