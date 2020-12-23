import copy
import timeit


def playCombat(player1_deck, player2_deck):
    while True:
        # collect cards from top of decks
        player1_card, player2_card = player1_deck.pop(0), player2_deck.pop(0)
        # determine round winner
        round_winner = player2_card > player1_card
        # add cards to round winners deck in the right order
        if round_winner:
            player2_deck += [player2_card, player1_card]
        else:
            player1_deck += [player1_card, player2_card]
        # check if any player has no cards left
        if not player2_deck:
            return


def playRecursiveCombat(player1_deck, player2_deck):
    played_rounds = set()
    while True:
        # endless games end with player 1 winning
        saved_decks = (tuple(player1_deck), tuple(player2_deck))
        if saved_decks in played_rounds:
            return 0
        played_rounds.add(saved_decks)
        # collect cards from top of decks
        player1_card, player2_card = player1_deck.pop(0), player2_deck.pop(0)
        # determine round winner via higher card
        if player1_card > len(player1_deck) or player2_card > len(player2_deck):
            round_winner = player2_card > player1_card
        # determine round winner via subgame
        else:
            subgame_player1_deck, subgame_player2_deck = player1_deck[:player1_card], player2_deck[:player2_card]
            if max(subgame_player1_deck) > max(subgame_player2_deck):
                round_winner = 0
            else:
                round_winner = playRecursiveCombat(subgame_player1_deck, subgame_player2_deck)
        # add cards to round winners deck in the right order
        if round_winner:
            player2_deck += [player2_card, player1_card]
        else:
            player1_deck += [player1_card, player2_card]
        # check if any player has no cards left
        if not player2_deck or not player1_deck:
            return round_winner


def countScore(deck):
    score = 0
    for multiplier, card in enumerate(reversed(deck), 1):
        score += card * multiplier
    return score


def run():
    x1 = [26, 8, 2, 17, 19, 29, 41, 7, 25, 33, 50, 16, 36, 37, 32, 4, 46, 12, 21, 48, 11, 6, 13, 23, 9]
    x2 = [27, 47, 15, 45, 10, 14, 3, 44, 31, 39, 42, 5, 49, 24, 22, 20, 30, 1, 35, 38, 18, 43, 28, 40, 34]
    y = playRecursiveCombat(x1, x2)


deck1 = [26, 8, 2, 17, 19, 29, 41, 7, 25, 33, 50, 16, 36, 37, 32, 4, 46, 12, 21, 48, 11, 6, 13, 23, 9]
deck2 = [27, 47, 15, 45, 10, 14, 3, 44, 31, 39, 42, 5, 49, 24, 22, 20, 30, 1, 35, 38, 18, 43, 28, 40, 34]
deck1_part2 = copy.deepcopy(deck1)
deck2_part2 = copy.deepcopy(deck2)

playCombat(deck1, deck2)
winner_part2 = playRecursiveCombat(deck1_part2, deck2_part2)
print("Part 1:", countScore(deck1))
print("Part 2:", countScore(deck1_part2))


setupcode = """
from __main__ import run
"""
print(timeit.timeit(stmt=run, setup=setupcode, number=1000)/1000)
