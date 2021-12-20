import math

with open('18.in') as infile:
    input = infile.read()


class Node(object):
    def __init__(self, value):
        self.value = value


class Number(object):
    def __init__(self, value):
        self.value = value


class Pair(object):
    def __init__(self, value):
        self.left = value[0]
        self.right = value[1]


def convert_pair(pair):
    value = pair.value
    if isinstance(value, Number):
        return value.value

    return [convert_pair(value.left), convert_pair(value.right)]


def get_sf_numbers_index(pair, i):
    if pair[i].isdigit():
        return Node(Number(int(pair[i]))), i + 1

    left = 0
    right = 0
    if pair[i] == '[':
        left, i = get_sf_numbers_index(pair, i + 1)

    if pair[i] == ',':
        right, i = get_sf_numbers_index(pair, i + 1)

    return Node(Pair([left, right])), i + 1


def get_sf_numbers(pair):
    numbers, i = get_sf_numbers_index(pair, 0)
    return numbers


def update_left_number(pair: list, stack: list, left: int):
    current = pair

    while len(stack) > 0 and stack[-1] == 0:
        stack.pop()

    if len(stack) == 0:
        return

    stack[-1] = 0

    for level in stack:
        current = current.value.left if level == 0 else current.value.right

    while isinstance(current.value, Pair):
        current = current.value.right

    current.value.value += left


def update_right_number(pair: list, stack: list, right: int):
    current = pair

    while len(stack) > 0 and stack[-1] == 1:
        stack.pop()

    if len(stack) == 0:
        return

    stack[-1] = 1

    for level in stack:
        current = current.value.left if level == 0 else current.value.right

    while isinstance(current.value, Pair):
        current = current.value.left

    current.value.value += right


def reduce_pair_once(pair: list, stack: list, allowSplit: bool):
    current = pair

    for level in stack:
        current = current.value.left if level == 0 else current.value.right

    curval = current.value

    if isinstance(curval, Pair):
        if isinstance(curval.left.value, Number) and isinstance(curval.right.value, Number):
            if len(stack) == 4:  # explode
                update_left_number(pair, stack.copy(), curval.left.value.value)
                update_right_number(pair, stack.copy(),
                                    curval.right.value.value)
                current.value = Number(0)

                return pair, 1

        stack.append(0)
        pair, action_type = reduce_pair_once(pair, stack, allowSplit)

        if action_type > 0:
            return pair, action_type
        stack.pop()

        stack.append(1)
        pair, action_type = reduce_pair_once(pair, stack, allowSplit)

        if action_type > 0:
            return pair, action_type
        stack.pop()

    elif allowSplit and isinstance(curval, Number):
        if curval.value > 9:     # split
            current.value = Pair([Node(Number(math.floor(
                curval.value / 2))), Node(Number(math.ceil(curval.value / 2)))])

            return pair, 2

    return pair, 0


def reduce_pair(pair):
    action_type = 1

    while action_type > 0:
        pair, action_type = reduce_pair_once(pair, [], False)
        if action_type == 0:
            pair, action_type = reduce_pair_once(pair, [], True)

    return pair


def sum_sf_numbers(num1, num2):
    return reduce_pair(Node(Pair([num1, num2])))


def sum_multi_sf_numbers(pairs):
    result = 0

    for pair in pairs:
        if result == 0:
            result = pair
        else:
            result = sum_sf_numbers(result, pair)

    return result


def magnitude(pair):
    if isinstance(pair, int):
        return pair

    return 3 * magnitude(pair[0]) + 2 * magnitude(pair[1])


def max_magnitude(lines):
    max_mag = 0

    for i in range(len(lines)):
        for j in range(len(lines)):
            if i != j:
                mag = magnitude(convert_pair(
                    sum_sf_numbers(get_sf_numbers(lines[i]), get_sf_numbers(lines[j]))))

                if mag > max_mag:
                    max_mag = mag

    return max_mag


pairs = list(map(get_sf_numbers, input.splitlines()))

# part 1
result = sum_multi_sf_numbers(pairs)
print(magnitude(convert_pair(result)))

# part 2
print(max_magnitude(input.splitlines()))
