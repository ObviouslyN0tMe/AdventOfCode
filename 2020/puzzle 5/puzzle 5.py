with open("puzzle input 5") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]
testdata = ["FBFBBFFRLR",  # row 44, column 5
            "BFFFBBFRRR",  # row 70, column 7
            "FFFBBBFRRR",  # row 14, column 7
            "BBFFBBFRLL"]  # row 102, column 4


def getRow(rowcode):
    front = 0
    back = 127
    remove = 64
    for x in rowcode:
        if x == "F":
            back -= remove
        else:
            front += remove
        remove *= 0.5
    return front


def getColumn(columncode):
    left = 0
    right = 127
    remove = 4
    for x in columncode:
        if x == "L":
            right -= remove
        else:
            left += remove
        remove *= 0.5
    return left


def getSeatIDs(seatcodes):
    seat_ids = []
    for seatcode in seatcodes:
        row_code = seatcode[0:7]
        column_code = seatcode[7:10]
        row = getRow(row_code)
        column = getColumn(column_code)
        seat_id = row * 8 + column
        seat_ids.append(seat_id)
    return seat_ids


def findMySeat(seat_ids):
    seat_ids.sort()
    for index, value in enumerate(seat_ids):
        diff = seat_ids[index + 1] - value
        if diff == 2:
            return value + 1

seat_ids = getSeatIDs(rawdata)
my_seat = findMySeat(seat_ids)
print(my_seat)
