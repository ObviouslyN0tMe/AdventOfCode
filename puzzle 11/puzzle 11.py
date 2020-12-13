# puzzle input
with open("puzzle input 11") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]
# test input
with open("test input 11") as file:
    testdata = [x.strip("\n") for x in file.readlines()]


def getOccupiedSeats(layout, row, seat):
    occseats = 0
    for y in range(-1, 2, 1):
        for x in range(-1, 2, 1):
            checked_seat = "."
            distance = 1
            if x == 0 and y == 0:
                checked_seat = ""
            while checked_seat == ".":
                y_move = y*distance
                x_move = x*distance
                row_checked = row + y_move
                seat_checked = seat + x_move
                if 0 <= row_checked < len(layout):
                    if 0 <= seat_checked < len(layout[row_checked]):
                        checked_seat = layout[row_checked][seat_checked]
                        if checked_seat == "#":
                            occseats += 1
                            break
                        distance += 1
                    else:
                        break
                else:
                    break
    return occseats


def getNewLayout(layout):
    new_layout = []
    for index_r, row in enumerate(layout):
        new_row = ""
        for index_s, status in enumerate(row):
            occseats = getOccupiedSeats(layout, index_r, index_s)
            if status == "L":
                if occseats == 0:
                    new_row += "#"
                else:
                    new_row += "L"
            elif status == "#":
                if occseats >= 5:
                    new_row += "L"
                else:
                    new_row += "#"
            else:
                new_row += "."
        new_layout.append(new_row)
    return new_layout


def findStableLayout(layout):
    old_layout = layout
    stable = False
    occseats = 0
    new_layout = []
    while not stable:
        new_layout = getNewLayout(old_layout)
        if old_layout == new_layout:
            stable = True
        else:
            old_layout = new_layout
    for row in new_layout:
        for seat in row:
            if seat == ".":
                occseats += 1
    return "Layout is now stable with " + str(occseats) + " occupied seats."


print(findStableLayout(rawdata))
