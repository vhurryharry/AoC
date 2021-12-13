import numpy as np

with open('9.in') as infile:
    input = infile.read()

lines = input.splitlines()

heightmap = []

for line in lines:
    heightmap.append(list(map(int, list(line))))


def check_basin_point(heightmap, basin, i, j):
    if basin[i][j] == 1:
        return

    basin[i][j] = 1

    if i > 0 and heightmap[i - 1][j] < 9 and heightmap[i - 1][j] > heightmap[i][j]:
        check_basin_point(heightmap, basin, i - 1, j)

    if j > 0 and heightmap[i][j - 1] < 9 and heightmap[i][j - 1] > heightmap[i][j]:
        check_basin_point(heightmap, basin, i, j - 1)

    if i < len(heightmap) - 1 and heightmap[i + 1][j] < 9 and heightmap[i + 1][j] > heightmap[i][j]:
        check_basin_point(heightmap, basin, i + 1, j)

    if j < len(heightmap[0]) - 1 and heightmap[i][j + 1] < 9 and heightmap[i][j + 1] > heightmap[i][j]:
        check_basin_point(heightmap, basin, i, j + 1)


def find_basin(heightmap, i, j):
    basin = [[0] * len(heightmap[0]) for i in range(len(heightmap))]

    check_basin_point(heightmap, basin, i, j)

    return sum(sum(basin, []))


def check_low_points(heightmap):
    total_risk = 0
    basins = []

    for i in range(len(heightmap)):
        for j in range(len(heightmap[i])):
            count = 0

            if i == 0 or heightmap[i - 1][j] > heightmap[i][j]:
                count += 1

            if j == 0 or heightmap[i][j - 1] > heightmap[i][j]:
                count += 1

            if i == len(heightmap) - 1 or heightmap[i + 1][j] > heightmap[i][j]:
                count += 1

            if j == len(heightmap[i]) - 1 or heightmap[i][j + 1] > heightmap[i][j]:
                count += 1

            if count == 4:
                total_risk += heightmap[i][j] + 1

                basin = find_basin(heightmap, i, j)

                if len(basins) < 3:
                    basins.append(basin)
                elif basins[0] < basin:
                    basins[0] = basin

                basins.sort()

    return total_risk, basins[0] * basins[1] * basins[2]


total_risk, basin = check_low_points(heightmap)

print(total_risk)
print(basin)
