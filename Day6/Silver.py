def fire(theList):
    theList.append(9)
    return 6


with open('input.txt') as f:
    line = f.read()

state = [int(x) for x in line.split(',')]

print(state)

for timer in range(80):
    state = [fire(state) if zero == 0 else zero - 1 for zero in state]
    print(state)

print(state)

print(len(state))

