with open("puzzleinput") as file:
    drawn_numbers = [int(x) for x in file.readline().split(",")]
    bingocard_lines = [[int(x) for x in line.strip().split()] for line in file if line != "\n"]

class bingoboard(object):
    def __init__(self, rows):
        self.rows = rows
        self.columns = []
        self.createColumn()

    def createColumn(self):
        for index in range(len(self.rows[0])):
            column = []
            for row in self.rows:
                column.append(row[index])
            self.columns.append(column)

    def removeNumber(self, number):
        for row in self.rows:
            if number in row:
                row.remove(number)
                if not row:
                    return self.calcScore(number)
        for column in self.columns:
            if number in column:
                column.remove(number)
                if not column:
                    return self.calcScore(number)

    def calcScore(self, last_number):
        score = 0
        for row in self.rows:
            score += sum(row)
        score *= last_number
        return score


bingoboards = []
board = []
for line in bingocard_lines:
    board.append(line)
    if len(board) == 5:
        bingoboards.append(bingoboard(board))
        board = []

scores = []
winning_boards = []
for number in drawn_numbers:
    for board in bingoboards:
        score = board.removeNumber(number)
        if score:
            scores.append(score)
            winning_boards.append(board)
    for board in winning_boards:
        bingoboards.remove(board)
    winning_boards = []

print("Part 1:", scores[0])
print("Part 2:", scores[-1])