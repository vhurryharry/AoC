
with open('1.in') as infile:
    input = infile.read()

x = list(map(int, input.split()))

count = 0

for i in range(len(x)):
    if i > 2 and x[i] > x[i-3]:
        count = count + 1

print(count)
