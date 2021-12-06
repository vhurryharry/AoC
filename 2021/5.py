import numpy as np
import re

with open('5.in') as infile:
    input = infile.read()

lines = input.splitlines()


def comprehend_coords(line):
    return list(map(int, re.split(' -> |,', line)))


coords = np.array(list(map(comprehend_coords, lines)))
vents = np.zeros(shape=(coords.max() + 1,
                        coords.max() + 1), dtype=int)


def hor_ver_mark(coords):
    for coord in coords:
        if coord[0] == coord[2]:
            if coord[1] < coord[3]:
                vents[coord[1]:coord[3] + 1, coord[0]] += 1
            else:
                vents[coord[3]:coord[1] + 1, coord[0]] += 1
        elif coord[1] == coord[3]:
            if coord[0] < coord[2]:
                vents[coord[1], coord[0]:coord[2] + 1] += 1
            else:
                vents[coord[1], coord[2]:coord[0] + 1] += 1


def diagonal_mark(coords):
    for coord in coords:
        if abs(coord[0] - coord[2]) == abs(coord[1] - coord[3]) and coord[0] != coord[2]:
            if coord[0] > coord[2]:
                coord[0], coord[2] = coord[2], coord[0]
                coord[1], coord[3] = coord[3], coord[1]

            new_vents = np.zeros(
                (abs(coord[0] - coord[2]) + 1, abs(coord[0] - coord[2]) + 1), int)

            if coord[1] < coord[3]:
                np.fill_diagonal(new_vents, 1)

                vents[coord[1]:coord[3] + 1, coord[0]:coord[2] + 1] += new_vents
            else:
                np.fill_diagonal(np.fliplr(new_vents), 1)

                vents[coord[3]:coord[1] + 1, coord[0]:coord[2] + 1] += new_vents


hor_ver_mark(coords)
diagonal_mark(coords)

print(vents)
print(np.count_nonzero(vents > 1))
