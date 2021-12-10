from collections import deque
with open("puzzleinput") as file:
    all_fish = [int(x) for x in file.readline().split(",")]

fish_list = deque([])
for x in range(9):
    fish_list.append(all_fish.count(x))

for day in range(80):
    baby_fish = []
    for fish in range(len(all_fish)):
        all_fish[fish] -= 1
        if all_fish[fish] == -1:
            all_fish[fish] = 6
            baby_fish.append(8)
    all_fish += baby_fish

print("Part 1:", len(all_fish))

# part 2
for day in range(256):
    babys = fish_list.popleft()
    fish_list.append(babys)
    fish_list[6] += babys

print("Part 2:", sum(fish_list))