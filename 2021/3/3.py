
with open('3.in') as infile:
    input = infile.read()

x = list(map(str, input.split()))


def part_one(x):
    gamma = 0
    epsilon = 0

    for i in range(len(x[0])):
        c0 = 0
        c1 = 0

        gamma *= 2
        epsilon *= 2

        for j in range(len(x)):
            if x[j][i] == '1':
                c1 += 1
            else:
                c0 += 1

        if c0 > c1:
            gamma += 1
        else:
            epsilon += 1

    print(gamma * epsilon)


def bit_criteria(arr, index, criteria):

    if len(arr) == 1:
        return arr[0]

    arr0 = []
    arr1 = []

    for i in range(len(arr)):
        if arr[i][index] == '1':
            arr1.append(arr[i])
        else:
            arr0.append(arr[i])

    if criteria == 1:
        if len(arr0) > len(arr1):
            return bit_criteria(arr0, index + 1, criteria)

        return bit_criteria(arr1, index + 1, criteria)
    else:
        if len(arr1) < len(arr0):
            return bit_criteria(arr1, index + 1, criteria)

        return bit_criteria(arr0, index + 1, criteria)


def part_two(x):
    oxygen = bit_criteria(x, 0, 1)
    co2 = bit_criteria(x, 0, 0)

    print(int(oxygen, 2) * int(co2, 2))


part_one(x)
part_two(x)
