import timeit
card_public_key = 11404017
door_public_key = 13768789


def getLoopSize(public_key):
    value = 1
    loop_size = 0
    while value != public_key:
        value *= 7
        value %= 20201227
        loop_size += 1
    return loop_size


def calcEncryptionKey(public_key, opposite_loop_size):
    encryption_key = 1
    for i in range(opposite_loop_size):
        encryption_key *= public_key
        encryption_key %= 20201227
    return encryption_key


# for timing
# short version
def runSuperShort():
    value, encryption_key = 1, 1
    while value != 11404017:
        value = (7 * value) % 20201227
        encryption_key = (13768789 * encryption_key) % 20201227
    print("Part 1:", encryption_key)


# long version
def run():
    card_loop_size = getLoopSize(card_public_key)
    solution = calcEncryptionKey(door_public_key, card_loop_size)
    print("Part 1:", solution)


print(timeit.timeit(stmt=run, number=10))
