with open('input.txt') as f:
    lines = f.read().splitlines()

board = [[0 for x in range(1000)] for y in range(1000)]
counter = 0

for line in lines:
    start = [int(x) for x in line.split()[0].split(',')]
    end = [int(x) for x in line.split()[2].split(',')]
    if start[0] == end[0]:
        if start[1] < end[1]:
            for i in range(start[1], end[1] + 1):
                board[i][start[0]] += 1
        elif start[1] > end[1]:
            for i in range(end[1], start[1] + 1):
                board[i][start[0]] += 1
    elif start[1] == end[1]:
        if start[0] < end[0]:
            for i in range(start[0], end[0] + 1):
                board[start[1]][i] += 1
        elif start[0] > end[0]:
            for i in range(end[0], start[0] + 1):
                board[start[1]][i] += 1
    elif abs(start[0] - end[0]) == abs(start[1] - end[1]):
        if start[0] > end[0] and start[1] > end[1]:
            for i in range((start[0] - end[0] + 1)):
                board[start[1] - i][start[0] - i] += 1
        elif start[0] > end[0] and start[1] < end[1]:
            for i in range((start[0] - end[0] + 1)):
                board[start[1] + i][start[0] - i] += 1
        elif start[0] < end[0] and start[1] > end[1]:
            for i in range((end[0] - start[0] + 1)):
                board[start[1] - i][start[0] + i] += 1
        elif start[0] < end[0] and start[1] < end[1]:
            for i in range((end[0] - start[0] + 1)):
                board[start[1] + i][start[0] + i] += 1



for boardRow in board:
    #print(boardRow)
    for boardCol in boardRow:
        if boardCol > 1:
            counter += 1

print(counter)
