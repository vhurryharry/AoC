import numpy as np

with open('19.in') as infile:
    input = infile.read()

sections = input.split('\n\n')


def parse_scanner(section):
    return np.array(list(map(lambda x: np.array(list(map(int, x.split(',')))), section.splitlines()[1:])))


scanners = list(map(parse_scanner, sections))

orientations = [
    np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
    np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]]),
    np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]]),
    np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]]),

    np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]]),
    np.array([[-1, 0, 0], [0, 0, -1], [0, -1, 0]]),
    np.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]]),
    np.array([[-1, 0, 0], [0, 0, 1], [0, 1, 0]]),

    np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]),
    np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]),
    np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1]]),
    np.array([[0, 0, -1], [1, 0, 0], [0, -1, 0]]),

    np.array([[0, 0, 1], [-1, 0, 0], [0, 1, 0]]),
    np.array([[0, 0, 1], [-1, 0, 0], [0, -1, 0]]),
    np.array([[0, -1, 0], [-1, 0, 0], [0, 0, -1]]),
    np.array([[0, 0, -1], [-1, 0, 0], [0, 1, 0]]),

    np.array([[0, 0, -1], [0, 1, 0], [1, 0, 0]]),
    np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]]),
    np.array([[0, 0, 1], [0, -1, 0], [1, 0, 0]]),
    np.array([[0, -1, 0], [0, 0, -1], [1, 0, 0]]),

    np.array([[0, 0, -1], [0, -1, 0], [-1, 0, 0]]),
    np.array([[0, -1, 0], [0, 0, 1], [-1, 0, 0]]),
    np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]]),
    np.array([[0, 1, 0], [0, 0, -1], [-1, 0, 0]])
]


def check_duplicates(beacons1, beacons2):
    for b1 in beacons1:
        for b2 in beacons2:
            offset = b1 - b2

            merged = np.concatenate((beacons1, beacons2 + offset))
            duplicates = len(merged) - len(np.unique(merged, axis=0))

            if duplicates >= 12:
                return offset

    return []


def check_scanners(scanner1, scanner2):
    for ori in orientations:
        offset = check_duplicates(scanner1, np.matmul(scanner2, ori))

        if len(offset) > 0:
            return ori, offset

    return [], []


def merge_scanners(scanners):
    for i in range(len(scanners)):
        for j in range(i + 1, len(scanners)):
            ori, offset = check_scanners(scanners[i], scanners[j])

            if len(ori) > 0 and len(offset) > 0:
                print(i, j, ori, offset)
                # merged = np.concatenate((merged, np.matmul(scanner, ori) + offset))

    # return merged


merge_scanners(scanners)
# merged = merge_scanners(scanners)
# print(len(merged))
# print(len(np.unique(merged, axis=0)))
