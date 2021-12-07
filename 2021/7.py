import numpy as np

with open('7.in') as infile:
    input = infile.read()

positions = np.array(list(map(int, input.split(','))))

min = np.min(positions)
max = np.max(positions)

minSum = -1

for i in range(min, max + 1):
    temp = positions - i
    sum = np.sum(np.abs(temp) * (np.abs(temp) + 1) / 2, dtype=int)
    minSum = sum if minSum == -1 or minSum > sum else minSum

print(minSum)
