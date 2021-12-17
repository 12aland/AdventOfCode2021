with open('input.txt') as f:
    lines = f.read().splitlines()

hpos = 0
aim = 0
depth = 0

for com in lines:
    z = com.split()
    if z[0] == 'forward':
        hpos += int(z[1])
        depth += int(z[1])*aim
    elif z[0] == 'up':
        aim -= int(z[1])
    elif z[0] == 'down':
        aim += int(z[1])

print(hpos)
print(depth)
print(hpos*depth)