# puzzle input
with open("puzzle input") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]
# test input
with open("test input") as file:
    testdata = [x.strip("\n") for x in file.readlines()]


def formatData(data):
    formated_data = []
    for line in data:
        # remove spaces
        line = line.replace(" ", "")
        row = []
        # collect list for row
        for char in line:
            # collect list for row
            if char == ")":
                in_par = []
                char = row.pop(-1)
                while char != "(":
                    in_par.append(char)
                    char = row.pop(-1)
                in_par = addBeforeMultiply(in_par)     # add before multiply in par
                in_par.reverse()
                row.append(in_par)
            else:
                row.append(char)
        row = addBeforeMultiply(row)     # add before multiply in row
        formated_data.append(row)
    return formated_data


def addBeforeMultiply(row):
    now = False
    new_row = []
    for char in row:
        if char == "+":
            now = True
        elif now:
            now = False
            left_nr = new_row.pop(-1)
            new_row.append([left_nr, "+", char])
        else:
            new_row.append(char)
    return new_row


def evaluateExpression(left, operator, right):
    while len(left) == 1 and isinstance(left, list):
        left = left[0]
    while len(right) == 1 and isinstance(right, list):
        right = right[0]
    if len(left) > 1:
        left = evaluateExpression(left[:-2], left[-2], left[-1])
    if len(right) > 1:
        right = evaluateExpression(right[:-2], right[-2], right[-1])
    if operator == "+":
        return str(int(left) + int(right))
    elif operator == "*":
        return str(int(left) * int(right))


def sumAllRows(rows):
    sum_rows = 0
    for row in rows:
        while len(row) == 1 and isinstance(row, list):
            row = row[0]
        sum_rows += int(evaluateExpression(row[:-2], row[-2], row[-1]))
    return sum_rows


rows = formatData(rawdata)
print(sumAllRows(rows))
