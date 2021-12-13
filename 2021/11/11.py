import numpy as np

with open('11.in') as infile:
    input = infile.read()

lines = input.splitlines()

matrix = []

for line in lines:
    matrix.append(list(map(int, list(line))))

matrix = np.array(matrix)


def flash_point(sx, sy, matrix, flashed):
    queue = [[sx, sy]]

    while len(queue) > 0:
        [x, y] = queue.pop(0)

        if flashed[x, y] == 1:
            continue

        matrix[x, y] += 1

        if matrix[x, y] > 9:
            flashed[x, y] = 1
            if x > 0:
                queue.append([x - 1, y])

                if y > 0:
                    queue.append([x - 1, y - 1])

                if y < len(matrix[0]) - 1:
                    queue.append([x - 1, y + 1])

            if x < len(matrix) - 1:
                queue.append([x + 1, y])

                if y > 0:
                    queue.append([x + 1, y - 1])

                if y < len(matrix[0]) - 1:
                    queue.append([x + 1, y + 1])

            if y > 0:
                queue.append([x, y - 1])

            if y < len(matrix[0]) - 1:
                queue.append([x, y + 1])


def one_step(matrix):
    flashed = np.zeros(shape=(len(matrix), len(matrix[0])))

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            flash_point(i, j, matrix, flashed)

    count = np.count_nonzero(matrix > 9)

    matrix[matrix > 9] = 0

    return count


def count_flashes(matrix, step):
    total_flashes = 0

    for i in range(step):
        total_flashes += one_step(matrix)

    return total_flashes


def count_first_sync(matrix):
    count = 0
    flashes = 0

    total_octopuses = np.shape(matrix)[0] * np.shape(matrix)[1]

    while flashes < total_octopuses:
        flashes = one_step(matrix)
        count += 1

    return count


# print(count_flashes(matrix, 100))
print(count_first_sync(matrix))
