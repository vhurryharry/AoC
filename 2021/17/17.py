import re

with open('17.in') as infile:
    input = infile.read()

area_values = list(map(int, re.split('target area: x=|, y=|\.\.', input)[1:]))

rx = [area_values[0], area_values[1]]
ry = [area_values[2], area_values[3]]


def find_max_height(ry):
    min_y = abs(ry[0])

    return (min_y - 1) * min_y / 2


# print(find_max_height(ry))


def check_shot(rx, ry, dx, dy):
    ox = 0
    oy = 0

    while ox <= rx[1] and oy >= ry[0]:
        if ox >= rx[0] and oy <= ry[1]:
            return True

        ox += dx
        oy += dy

        dx = 0 if dx == 0 else dx - 1
        dy -= 1

    return False


def count_velocities(rx, ry):
    count = 0

    for dx in range(1, rx[1] + 1):
        for dy in range(ry[0], -ry[0] + 1):
            if check_shot(rx, ry, dx, dy):
                count += 1

    return count


print(count_velocities(rx, ry))
