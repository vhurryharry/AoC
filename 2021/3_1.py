
with open('3.in') as infile:
    input = infile.read()

x = list(map(str, input.split()))


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


oxygen = bit_criteria(x, 0, 1)
co2 = bit_criteria(x, 0, 0)

print(int(oxygen, 2) * int(co2, 2))
