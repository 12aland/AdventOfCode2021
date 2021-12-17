with open('input.txt') as f:
    lines = f.read().splitlines()

gamma = ''
epsilon = ''

for index in range(0, len(lines[0])):
    zero = 0
    one = 0
    for line in lines:
        if line[index] == '0':
            zero += 1
        elif line[index] == '1':
            one += 1

    if zero > one:
        print('works')
        gamma += '0'
        epsilon += '1'
    elif one > zero:
        gamma += '1'
        epsilon += '0'
    print(gamma)

print('Gamma:', gamma)
print('Epsilon:', epsilon)
print('Consumption:', int(gamma,2)*int(epsilon,2))

