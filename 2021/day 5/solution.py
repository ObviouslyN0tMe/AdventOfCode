from _collections import defaultdict
with open("puzzleinput") as file:
    data = [x.strip("\n").split(" -> ") for x in file.readlines()]

# format and sort lines
lines_diagonal = []
lines_vertical = []
lines_horizontal = []

for line in data:
    end1 = [int(x) for x in line[0].split(",")]
    end2 = [int(x) for x in line[1].split(",")]
    new_line = (end1, end2)
    if new_line[0][0] == new_line[1][0]:
        lines_vertical.append(new_line)
    elif new_line[0][1] == new_line[1][1]:
        lines_horizontal.append(new_line)
    else:
        lines_diagonal.append(new_line)

# draw lines on a board
board = defaultdict(int)
end = 0
start = 0

# draw horizontal lines
for line in lines_horizontal:
    y = line[0][1]
    if line[0][0] > line[1][0]:
        start = line[1][0]
        end = line[0][0]
    else:
        start = line[0][0]
        end = line[1][0]
    for x in range(start, end+1):
        board[(x, y)] += 1

# draw vertical lines

for line in lines_vertical:
    x = line[0][0]
    if line[0][1] > line[1][1]:
        start = line[1][1]
        end = line[0][1]
    else:
        start = line[0][1]
        end = line[1][1]
    for y in range(start, end+1):
        board[(x, y)] += 1

# count how many overlaps
counter = 0
for overlaps in board.values():
    if overlaps > 1:
        counter += 1

print("Part 1:", counter)
