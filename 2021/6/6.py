import numpy as np

with open('6.in') as infile:
    input = infile.read()


def using_numpy(input):
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


def without_numpy(input):
    lanternfish = list(map(int, input.split(',')))
    ages = [lanternfish.count(x) for x in range(9)]

    for day in range(1000):
        ages.append(ages.pop(0))
        ages[6] += ages[8]

    print(sum(ages))


without_numpy(input)
