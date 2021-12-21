
with open('20.in') as infile:
    input = infile.read()

sections = input.split('\n\n')
algorithm = sections[0]
image = list(map(list, sections[1].splitlines()))


def process(image, algorithm, outside):
    new_image = [['.'] * (len(image[0]) + 2) for i in range(len(image) + 2)]

    dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1],
            [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]

    for i in range(len(new_image)):
        for j in range(len(new_image[0])):
            value = 0

            for dir in dirs:
                di = i + dir[0]
                dj = j + dir[1]
                point = outside

                if di >= 1 and dj >= 1 and di <= len(image) and dj <= len(image[0]):
                    point = 0 if image[di - 1][dj - 1] == '.' else 1

                value = value * 2 + point

            new_image[i][j] = algorithm[value]

    new_outside = algorithm[0] if outside == 0 else algorithm[-1]
    new_outside = 0 if new_outside == '.' else 1
    return new_image, new_outside


new_image = image
outside = 0

for i in range(50):
    new_image, outside = process(new_image, algorithm, outside)
    print(i)


print(sum(x.count('#') for x in new_image))
