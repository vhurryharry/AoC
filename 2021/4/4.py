import numpy as np

with open('4.in') as infile:
    input = infile.read()

lines = input.splitlines()

numbers = np.array(list(map(int, lines[0].split(','))))
matrixes = []

for m in range(1, len(lines), 6):
    matrix = []
    for l in range(1, 6):
        matrix.append(list(map(int, lines[m + l].split())))

    matrixes.append(matrix)

matrixes = np.array(matrixes)


def check_matrix(matrix, numbers):
    for line in matrix:
        if np.all(np.in1d(line, numbers)):
            return True


def check_bingo(matrix, numbers):
    return check_matrix(matrix, numbers) or check_matrix(matrix.T, numbers)


def calculate_bingo(matrix, numbers):
    print(matrix, numbers)
    return (np.sum(matrix) - np.sum(numbers[np.in1d(numbers, matrix)])) * numbers[-1]


def check_numbers(matrixes, numbers):
    for matrix in matrixes:
        if(check_bingo(matrix, numbers)):
            return calculate_bingo(matrix, numbers)

    return -1


def check_matrixes(matrixes, numbers):
    for i in range(5, len(numbers)):
        bingo = check_numbers(matrixes, numbers[0:i])
        if bingo >= 0:
            return bingo

    return -1


def check_not_bingo_matrixes(matrixes, numbers):
    not_bingo = np.ones(len(matrixes), dtype=bool)

    for i, matrix in enumerate(matrixes):
        not_bingo[i] = False if check_bingo(matrix, numbers) else True

    return not_bingo


def check_matrixes_reverse(matrixes, numbers):
    for i in range(5, len(numbers)):
        new_matrixes = matrixes[check_not_bingo_matrixes(
            matrixes, numbers[0:i])]

        if len(new_matrixes) == 0:
            return calculate_bingo(matrixes[-1], numbers[0:i])
        else:
            matrixes = new_matrixes

    return -1


# print(check_matrixes(matrixes, numbers))
print(check_matrixes_reverse(matrixes, numbers))
