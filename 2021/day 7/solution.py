with open("puzzleinput") as file:
    crab_positions = [int(x) for x in file.readline().split(",")]

crab_positions.sort()
perfect_position = crab_positions[len(crab_positions)//2]

print("Part 1:", perfect_position)