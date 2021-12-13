import numpy as np
import re

from numpy.core.fromnumeric import shape

with open('13.in') as infile:
    input = infile.read()

sections = input.split('\n\n')


def make_paper(section):
    points = []

    lines = section.splitlines()

    for line in lines:
        points.append(list(map(int, line.split(','))))

    points = np.array(points)
    size = np.amax(points, axis=0)

    paper = np.zeros(shape=(size[1] + 1, size[0] + 1))

    for point in points:
        paper[point[1], point[0]] = 1

    return paper


def get_folds(section):
    lines = section.splitlines()
    folds = []

    for line in lines:
        fold = re.split('fold along |=', line)[1:]
        fold[1] = int(fold[1])
        folds.append(fold)

    return folds


def fold_paper_once(paper, fold):
    if fold[0] == 'x':
        sx = max(fold[1], len(paper[0]) - fold[1] - 1)
        ox = max(0, len(paper[0]) - 2 * fold[1] - 1)
        sy = len(paper)
    else:
        sx = len(paper[0])
        sy = max(fold[1], len(paper) - fold[1] - 1)
        oy = max(0, len(paper) - 2 * fold[1] - 1)

    new_paper = np.zeros(shape=(sy, sx))

    for i in range(sy):
        for j in range(sx):
            if fold[0] == 'x':
                new_paper[i, j] = 0

                if 2 * sx - j + ox < len(paper[0]):
                    new_paper[i, j] += paper[i, 2 * sx - j + ox]
                if j >= ox:
                    new_paper[i, j] += paper[i, j - ox]
            else:
                new_paper[i, j] = 0

                if 2 * sy - i + oy < len(paper):
                    new_paper[i, j] += paper[2 * sy - i + oy, j]
                if i >= oy:
                    new_paper[i, j] += paper[i - oy, j]

    return new_paper


def fold_paper(paper, folds):
    new_paper = np.copy(paper)
    for fold in folds:
        new_paper = fold_paper_once(new_paper, fold)

    return new_paper


def format_point(value):
    if value > 0:
        return '#'
    return ' '


paper = make_paper(sections[0])
folds = get_folds(sections[1])

# new_paper = fold_paper_once(paper, folds[0])
# count_dots = np.count_nonzero(new_paper > 0)
# print(count_dots)

new_paper = fold_paper(paper, folds)


for row in new_paper:
    print(''.join(list(map(format_point, row))))
