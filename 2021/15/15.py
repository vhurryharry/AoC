import numpy as np
import bisect

with open('15.in') as infile:
    input = infile.read()

lines = input.splitlines()

matrix = []

for line in lines:
    matrix.append(list(map(int, list(line))))

matrix = np.array(matrix)


def navigate(matrix):
    queue = [[0, 0, 0]]

    distance = np.copy(matrix)
    distance.fill(np.sum(matrix))
    distance[0, 0] = 0

    added = np.zeros(np.shape(matrix))
    added[0, 0] = 1

    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    while len(queue) > 0:
        [value, x, y] = queue.pop(0)

        for dir in dirs:
            nx = x + dir[0]
            ny = y + dir[1]

            if nx >= 0 and nx < len(matrix) and ny >= 0 and ny < len(matrix[0]):
                distance[nx, ny] = min(
                    distance[nx, ny], value + matrix[nx, ny])
                if added[nx, ny] == 0:
                    bisect.insort(queue, [distance[nx, ny], nx, ny])
                    added[nx, ny] = 1

    return distance


def expand_matrix(matrix):
    xlen = len(matrix)
    ylen = len(matrix[0])
    new_matrix = np.zeros(shape=(xlen * 5, ylen * 5), dtype=int)

    for i in range(5):
        for j in range(5):
            new_matrix[xlen * i: xlen *
                       (i + 1), ylen * j: ylen * (j + 1)] = (matrix + i + j + 8) % 9 + 1

    return new_matrix


# distance = navigate(matrix)
# print(distance)


new_matrix = expand_matrix(matrix)
distance = navigate(new_matrix)
print(distance[-1, -1])
