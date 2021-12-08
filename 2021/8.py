
import numpy as np

with open('8.in') as infile:
    input = infile.read()

lines = input.splitlines()

digits = [[part.split(' ') for part in line.split(' | ')] for line in lines]


def count_unique_numbers(digits):
    count = 0

    for output in digits:
        count += sum(map(lambda digit: len(digit) == 2 or len(digit) ==
                         4 or len(digit) == 3 or len(digit) == 7, output[1]))
    return count


def analyse_pattern(line):
    digit_patterns = [{1, 2, 3, 4, 5, 6}, {2, 3}, {0, 1, 2, 4, 5}, {0, 1, 2, 3, 4}, {0, 2, 3, 6}, {
        0, 1, 3, 4, 6}, {0, 1, 3, 4, 5, 6}, {1, 2, 3}, {0, 1, 2, 3, 4, 5, 6}, {0, 1, 2, 3, 4, 6}]
    pattern = np.array(list(map(lambda x: set(x), line[0])))
    c = [''] * 7

    one = pattern[[i for i, item in enumerate(pattern) if len(item) == 2][0]]
    four = pattern[[i for i, item in enumerate(pattern) if len(item) == 4][0]]
    seven = pattern[[i for i, item in enumerate(pattern) if len(item) == 3][0]]
    eight = pattern[[i for i, item in enumerate(pattern) if len(item) == 7][0]]

    six_ones = pattern[[i for i, item in enumerate(pattern) if len(item) == 6]]
    six_intersection = six_ones[0].intersection(
        six_ones[1]).intersection(six_ones[2])

    c[1] = list(seven.difference(one))[0]
    c[2] = list(one.difference(six_intersection))[0]
    c[3] = list(one.intersection(six_intersection))[0]

    c[0] = list(four.difference(six_intersection).difference(set(c)))[0]
    c[6] = list(four.difference(set(c)))[0]
    c[4] = list(six_intersection.difference(set(c)))[0]
    c[5] = list(eight.difference(set(c)))[0]

    output = np.array(
        list(map(lambda x: np.array(list(set(x))), line[1])), dtype=object)

    number = 0

    for digit in output:
        indices = set(np.where(np.in1d(c, digit))[0])
        number = number * 10 + digit_patterns.index(indices)

    return number


sum = sum(analyse_pattern(digit) for digit in digits)
print(sum)
# print(count_unique_numbers(digits))
