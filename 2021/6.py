import numpy as np

with open('6.in') as infile:
    input = infile.read()

lanternfish = np.array(list(map(int, input.split(','))))


def init_ages(lanternfish):
    ages = np.zeros(9, int)
    for i in range(9):
        ages[i] = np.count_nonzero(lanternfish == i)

    return ages


def new_day(ages):
    ages = np.roll(ages, -1)
    ages[6] += ages[8]

    return ages


def count_lanternfish(ages, days):
    for day in range(days):
        ages = new_day(ages)

    return np.sum(ages)


ages = init_ages(lanternfish)

print(count_lanternfish(ages, 256))
