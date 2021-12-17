with open('input.txt') as f:
    lines = f.read().splitlines()

lines = [int(i) for i in lines]
counter = 0
for x in range(1, len(lines)):
    if lines[x] > lines[x - 1]:
        counter += 1
print(counter)
