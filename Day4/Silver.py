class Board:
    def __init__(self,boardArray):
        self.boardArray = boardArray
        print(self.boardArray)

with open('input.txt') as f:
    lines = f.read().splitlines()

numbers = lines.pop(0)
boards = []
temp = []
for lineNum in range(1,len(lines)+1):
    if not lineNum%6 == 0:
        temp.append([int(x) for x in lines[lineNum].split()])
        #temp.append([lines[lineNum]])
    else:
        boards.append(Board(temp))
        temp = []

#print(lines[1].split())
#boards.append(temp)

z = [[3,2]]

if 2 in z:
    print('aa')

print(numbers.split())

print()