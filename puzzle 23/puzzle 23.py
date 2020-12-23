import timeit

rawdata = [5, 8, 6, 4, 3, 9, 1, 7, 2]
testdata = [3, 8, 9, 1, 2, 5, 4, 6, 7]


def formatData(setup, part):
    setup_dict = {}
    for index, label in enumerate(setup):
        setup_dict[label] = setup[(index + 1) % len(setup)]
    if part == 2:
        for x in range(10, 1000000):
            setup_dict[x] = x + 1
        setup_dict[setup[-1]] = 10
        setup_dict[1000000] = setup[0]
    return setup_dict


def playCrabCups(current_setup, moves, start_cup):
    modulo = len(current_setup)
    current_cup = start_cup
    for move in range(moves):
        # collect 3 cups in list
        three_cups = []
        next_cup = current_cup
        for x in range(0, 3):
            next_cup = current_setup[next_cup]
            three_cups.append(next_cup)
        # link current cup to 4th cup after it
        current_setup[current_cup] = current_setup[three_cups[-1]]
        # find destination cup
        destination_cup = current_cup
        while True:
            destination_cup = (destination_cup - 1)
            if not destination_cup:
                destination_cup = modulo
            if destination_cup not in three_cups:
                break
        # insert 3 cups
        current_setup[three_cups[2]] = current_setup[destination_cup]
        current_setup[destination_cup] = three_cups[0]
        # get new current cup
        current_cup = current_setup[current_cup]
    return current_setup


def getSolutionPart1(setup):
    solution = ""
    next_cup = 1
    for i in range(1, 9):
        next_cup = setup[next_cup]
        solution += str(next_cup)
    return solution


def getSolutionPart2(setup):
    start = setup[1]
    solution = start * setup[start]
    return solution


# part 1
starting_setup_1 = formatData(rawdata, 1)
final_setup_1 = playCrabCups(starting_setup_1, 100, rawdata[0])
print(getSolutionPart1(final_setup_1))


# for timing
def run():
    # part 2
    starting_setup_2_run = formatData(rawdata, 2)
    final_setup_2_run = playCrabCups(starting_setup_2_run, 10000000, rawdata[0])
    print(getSolutionPart2(final_setup_2_run))


setupcode = """
from __main__ import run
"""

print(timeit.timeit(stmt=run, setup=setupcode, number=1))
