import statistics

with open('input.txt') as f:
    line = f.read()

counter = 0
median = 0

state = [int(x) for x in line.split(',')]

median = statistics.median(state)

for x in state:
    counter+=abs(x-median)

print(counter)
