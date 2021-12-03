
with open('3.in') as infile:
    input = infile.read()

x = list(map(str, input.split()))

gamma = 0
epsilon = 0

for i in range(len(x[0])):
    c0 = 0
    c1 = 0

    gamma *= 2
    epsilon *= 2

    for j in range(len(x)):
        if x[j][i] == '1':
            c1 += 1
        else:
            c0 += 1

    if c0 > c1:
        gamma += 1
    else:
        epsilon += 1

print(gamma * epsilon)
