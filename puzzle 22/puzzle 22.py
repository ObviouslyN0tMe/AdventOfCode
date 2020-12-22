import copy
import timeit

# puzzle input
with open("puzzle input") as file:
    rawdata = [x.strip(":\n") for x in file.readlines()]
# test input
with open("test input") as file:
    testdata = [x.strip(":\n") for x in file.readlines()]

start = timeit.default_timer()


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
        played_cards = []
        for player in player_decks.keys():
            played_cards.append(player_decks[player].pop(0))
        # determine round winner
        round_winner = "Player " + str(played_cards.index(max(played_cards)) + 1)
        # add cards to round winners deck in the right order
        if round_winner == "Player 2":
            played_cards.reverse()
        player_decks[round_winner] += played_cards
        # check if any player has no cards left
        for player in player_decks.keys():
            if len(player_decks[player]) == 0:
                player_decks.pop(player)
                return player_decks[round_winner]


def playRecursiveCombat(player_decks):
    played_rounds = player_decks["Player 1"].copy() + [""] + player_decks["Player 2"].copy()
    subgame_decks = {}
    while True:
        # collect cards from top of decks
        played_cards = [player_decks["Player 1"].pop(0), player_decks["Player 2"].pop(0)]
        # determine round winner via subgame or higher card
        if played_cards[0] <= len(player_decks["Player 1"]) and played_cards[1] <= len(player_decks["Player 2"]):
            subgame_decks["Player 1"] = player_decks["Player 1"][:played_cards[0]].copy()
            subgame_decks["Player 2"] = player_decks["Player 2"][:played_cards[1]].copy()
            if max(subgame_decks["Player 1"]) > max(subgame_decks["Player 2"]):
                round_winner = "Player 1"
            else:
                useless, round_winner = playRecursiveCombat(subgame_decks)
        else:
            round_winner = "Player " + str(played_cards.index(max(played_cards)) + 1)
        # add cards to round winners deck in the right order
        if round_winner == "Player 2":
            played_cards.reverse()
        player_decks[round_winner] += played_cards
        # check if any player has no cards left
        if len(player_decks["Player 1"]) == 0 or len(player_decks["Player 2"]) == 0:
            return player_decks, round_winner
        # endless games end with player 1 winning
        saved_decks = player_decks["Player 1"].copy() + [""] + player_decks["Player 2"].copy()
        if saved_decks in played_rounds:
            return player_decks, "Player 1"
        else:
            played_rounds.append(saved_decks)


def countScore(deck):
    score = 0
    multiplier = 1
    for card in reversed(deck):
        score += card * multiplier
        multiplier += 1
    return score


decks = formatData(rawdata)
decks_part2 = copy.deepcopy(decks)
winner_deck = playCombat(decks)
print("Part 1:", countScore(winner_deck))
end_decks, winner = playRecursiveCombat(decks_part2)
print("Part 2:", countScore(end_decks[winner]))

stop = timeit.default_timer()
print('Time: ', stop - start)
