with open('input.txt') as f:
    lines = f.read().splitlines()

lines = [int(i) for i in lines]
counter = 0
for x in range(3, len(lines)):
    defender = lines[x-3]+lines[x-2]+lines[x-1]
    challenger = lines[x-2]+lines[x-1]+lines[x-0]
    if challenger > defender:
        counter += 1
print(counter)
