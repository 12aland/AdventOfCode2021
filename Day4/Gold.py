with open('input.txt') as f:
    lines = f.read().splitlines()

oxygen = ''
co2 = ''

can = lines

for index in range(0, len(can[0])):
    ztemp = []
    otemp = []
    zero = 0
    one = 0

    if len(can) == 1:
        break

    for line in can:
        if line[index] == '0':
            zero += 1
            ztemp.append(line)
        elif line[index] == '1':
            one += 1
            otemp.append(line)

    if zero > one:
        can = ztemp
    elif one >= zero:
        can = otemp

oxygen = can
can = lines

for index in range(0, len(can[0])):
    ztemp = []
    otemp = []
    zero = 0
    one = 0

    if len(can) == 1:
        break


    for line in can:
        if line[index] == '0':
            zero += 1
            ztemp.append(line)
        elif line[index] == '1':
            one += 1
            otemp.append(line)

    if zero <= one:
        can = ztemp
    elif one < zero:
        can = otemp


co2 = can




print('Oxygen:', oxygen, int(oxygen[0], 2))
print('Co2:', co2, int(co2[0], 2))
print('Consumption:', int(oxygen[0], 2) * int(co2[0], 2))

