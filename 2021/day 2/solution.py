with open("puzzleinput") as file:
    data = [(direction, int(distance)) for direction, distance in [x.split() for x in file.readlines()]]

# Part 1
position = [0, 0]
for command in data:
    if command[0] == "forward":
        position[0] += command[1]
    elif command[0] == "up":
        position[1] -= command[1]
    elif command[0] == "down":
        position[1] += command[1]

print("Part 1: " + str(position[0]*position[1]))

# Part 2
position = [0, 0]
aim = 0
for command in data:
    if command[0] == "forward":
        position[0] += command[1]
        position[1] += command[1]*aim
    elif command[0] == "up":
        aim -= command[1]
    elif command[0] == "down":
        aim += command[1]

print("Part 2: " + str(position[0]*position[1]))
