import re
import numpy as np
from copy import deepcopy

with open('23.in') as infile:
    input = infile.read()

lines = input.splitlines()
positions = [list(filter(None, re.split('#', lines[2]))),
             list(filter(None, re.split('#| ', lines[3])))]

amphipods = np.zeros((3, 11), dtype=int)

for i in range(len(positions)):
    room = 2
    for pos in positions[i]:
        if pos == 'A':
            amphipods[i + 1, room] = 1
        elif pos == 'B':
            amphipods[i + 1, room] = 2
        elif pos == 'C':
            amphipods[i + 1, room] = 3
        else:
            amphipods[i + 1, room] = 4

        room += 2


destination = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 0],
    [0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 0]
])
min_energe = -1


def hallway_to_room(amphipods: np.array, hallway_pos: int):
    amp = amphipods[0, hallway_pos]
    distance = 0

    if amp * 2 < hallway_pos:
        if len(np.where(amphipods[0, amp * 2:hallway_pos] > 0)[0]) > 0:
            return -1, -1, -1

        distance = hallway_pos - amp * 2

    if amp * 2 > hallway_pos:
        if len(np.where(amphipods[0, hallway_pos + 1:amp * 2] > 0)[0]) > 0:
            return -1, -1, -1

        distance = amp * 2 - hallway_pos

    if (amphipods[1, amp * 2] != 0 and amphipods[1, amp * 2] != amp) or (amphipods[2, amp * 2] != 0 and amphipods[2, amp * 2] != amp):
        return -1, -1, -1

    depth = 1
    if amphipods[2, amp * 2] == 0:
        depth = 2

    distance += depth

    return pow(10, amp - 1) * distance, depth, amp * 2


def room_to_hallway(amphipods: np.array, ai: int, aj: int):
    if amphipods[ai - 1, aj] != 0:
        return []

    if amphipods[ai, aj] * 2 == aj:
        if ai == 2:
            return []

        if amphipods[ai, aj] == amphipods[ai + 1, aj]:
            return []

    left = np.where(amphipods[0, :aj] > 0)[0]
    right = np.where(amphipods[0, aj + 1:] > 0)[0]

    left_empty = max(left) + 1 if len(left) > 0 else 0
    right_empty = min(right) - 1 + aj + 1 if len(right) > 0 else 10

    routes = []
    for i in range(left_empty, right_empty + 1):
        if i % 2 == 1 or i < 2 or i > 8:
            routes.append([pow(10, amphipods[ai, aj] - 1)
                          * (abs(i - aj) + ai), i])

    return routes


def move(amphipods: np.array, energe: int):
    global min_energe

    if min_energe > 0 and energe >= min_energe:
        return

    if np.array_equal(destination, amphipods):
        if min_energe == -1 or min_energe > energe:
            min_energe = energe

            print(min_energe)

        return

    for i in range(1, 3):
        for j in np.where(amphipods[i] > 0)[0]:
            routes = room_to_hallway(amphipods, i, j)

            for route in routes:
                new_amphipods = np.copy(amphipods)

                new_amphipods[0, route[1]
                              ], new_amphipods[i, j] = new_amphipods[i, j], new_amphipods[0, route[1]]

                move(new_amphipods, energe + route[0])

    for i in np.where(amphipods[0] > 0)[0]:
        consumed_energe, ai, aj = hallway_to_room(amphipods, i)

        if consumed_energe >= 0:
            new_amphipods = np.copy(amphipods)

            new_amphipods[0, i], new_amphipods[ai,
                                               aj] = new_amphipods[ai, aj], new_amphipods[0, i]

            move(new_amphipods, energe + consumed_energe)


move(amphipods, 0)
