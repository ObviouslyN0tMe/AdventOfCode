rawdata = [0, 20, 7, 16, 1, 18, 15]
testdata = [0, 3, 6]


def playGame(starting_numbers, game_lengh):
    mentioned_numbers = {}
    for index, value in enumerate(starting_numbers[:-1]):
        mentioned_numbers[value] = index + 1
    turn = len(starting_numbers)
    last_number = starting_numbers[-1]
    for i in range(turn, game_lengh, 1):
        if last_number not in mentioned_numbers.keys():
            mentioned_numbers[last_number] = i
            last_number = 0
        else:
            new_number = i - mentioned_numbers[last_number]
            mentioned_numbers[last_number] = i
            last_number = new_number
    return last_number


print(playGame(rawdata, 30000000))
