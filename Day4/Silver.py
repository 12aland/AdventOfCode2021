import copy


# Creates Board
class Board:
    def __init__(self):
        self.num2coordict = {}
        self.xdict = {}
        self.ydict = {}
        self.listofdicts = [self.xdict, self.ydict]
        self.rows = []
        self.tempBoard = []

    def addRow(self, row):
        ycoord = len(self.rows)
        self.num2coordict.update({key: (xcoord, ycoord) for xcoord, key in enumerate(row)})
        self.rows.append(row)

    def addCoords(self, x, y, list):
        xcount = list[0].setdefault(x, 0)
        xcount += 1
        list[0].update({x: xcount})
        ycount = list[1].setdefault(y, 0)
        ycount += 1
        list[1].update({y: ycount})

    def markNum(self, num):
        x, y = self.num2coordict.get(num)
        self.tempBoard[y][x] = 0
        self.addCoords(x, y, self.listofdicts)
        if self.check():
            print(self.answer(num))
            return True

    def check(self):
        for dict in self.listofdicts:
            if 5 in dict.values():
                return True

    def answer(self, lastnum):
        counter = 0
        for rows in self.tempBoard:
            for num in rows:
                counter += num
        print('Last Num is', lastnum)
        return lastnum * counter

    def showBoards(self):
        for row in self.rows:
            print(row)
        print('-----------------------------')
        for row in self.tempBoard:
            print(row)

    def finalize(self):
        self.tempBoard = copy.deepcopy(self.rows)


with open('input.txt') as f:
    lines = f.read().splitlines()

numbers = lines.pop(0)
# numbers = numbers.split(',')
numbers = [int(x) for x in numbers.split(',')]
lines.pop(0)
boardList = []
boardIndexes = []
numdict = {}
board = Board()
for lineNum, line in enumerate(lines, start=1):
    if lineNum % 6 == 0:
        board.finalize()
        boardList.append(board)
        board = Board()

    elif not lineNum % 6 == 0:
        boardLine = [int(x) for x in line.split()]
        for num in boardLine:
            boardIndexes = numdict.setdefault(num, [])
            boardIndexes.append(int(lineNum / 6))
            numdict.update({num: boardIndexes})
        board.addRow(boardLine)

board.finalize()
boardList.append(board)
board = Board()


# for board in boardList:
# print(numdict)

def marker():
    for callNum in numbers:  # Go through the Bingo Line
        for indexNum in numdict.get(callNum):  # Find the Boards from the Dictionary
            if boardList[indexNum].markNum(callNum):  # Mark the numbers on the board
                print('Success')
                boardList[indexNum].showBoards()
                return


marker()
