# Creates Board
class Board:
    def __init__(self):
        self.num2coordict = {}
        self.indexdict = {}
        self.rows = []

    def addRow(self, row):
        ycoord = len(self.rows)
        self.num2coordict.update({key: (xcoord, ycoord) for xcoord, key in enumerate(row)})
        self.rows.append(row)

    def check(self):
        return True


with open('input.txt') as f:
    lines = f.read().splitlines()

numbers = lines.pop(0)
lines.pop(0)
boardList = []
boardIndexes = []
numdict = {}
board = Board()

for lineNum, line in enumerate(lines, start=1):
    if lineNum % 6 == 0:
        boardList.append(board)
        board = Board()

    elif not lineNum % 6 == 0:
        boardLine = [int(x) for x in line.split()]
        for num in boardLine:
            boardIndexes = numdict.setdefault(num, [])
            boardIndexes.append(int(lineNum / 6))
            numdict.update({num: boardIndexes})
        board.addRow(boardLine)

boardList.append(board)

print(numdict)
print(numbers.split())

for board in boardList:
    print(board.num2coordict)
