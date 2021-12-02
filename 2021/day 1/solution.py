with open("puzzleinput") as file:
    data = [int(x.strip("\n")) for x in file.readlines()]

count = 0
for index in range(1, len(data)):
    if data[index] > data[index-1]:
        count += 1

print("Part 1: " + str(count))

# part 2
with open("puzzleinput") as file:
    data = [int(x.strip("\n")) for x in file.readlines()]

count = 0
for index in range(3, len(data)):
    if data[index] > data[index-3]:
        count += 1

print("Part 1: " + str(count))

