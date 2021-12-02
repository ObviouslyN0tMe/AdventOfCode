card_public_key = 11404017
door_public_key = 13768789
loop_size = 0
x = 1

# Tür loop size
while x != door_public_key:
    x *= 7
    x %= 20201227
    loop_size += 1

# encrypo
x = 1
while loop_size > 0:
    x *= card_public_key
    x %= 20201227
    loop_size -= 1

print(x)
