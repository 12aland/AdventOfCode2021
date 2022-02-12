with open('input.txt') as f:
    line = f.read()

state = {x: 0 for x in range(9)}
counter = 0

print(line)

for time in line.split(','):
    state.update({int(time): state.get(int(time)) + 1})

print(state)

for timer in range(256):
    dupe = state.copy()
    state = {x:dupe.get(x+1) for x in range(0,8)}
    state.update({8:dupe.get(0)})
    state.update({6:(dupe.get(0)+dupe.get(7))})

    print(state)


for x in state.values():
    counter += x

print(counter)
