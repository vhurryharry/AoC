import math

with open('18.test3') as infile:
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


def reduce_pair_once(pair: list, stack: list):
    current = pair

    for level in stack:
        current = current.value.left if level == 0 else current.value.right

    curval = current.value
    if isinstance(curval, Pair):
        if isinstance(curval.left.value, Number) and isinstance(curval.right.value, Number):
            if len(stack) >= 4:  # explode
                update_left_number(pair, stack.copy(), curval.left.value.value)
                update_right_number(pair, stack.copy(),
                                    curval.right.value.value)
                current.value = Number(0)

                return pair, 1

        if isinstance(curval.left.value, Number):
            if curval.left.value.value > 9:
                curval.left.value = Pair([Node(Number(math.floor(
                    curval.left.value.value / 2))), Node(Number(math.ceil(curval.left.value.value / 2)))])

                return pair, 2

        if isinstance(curval.right.value, Number):
            if curval.right.value.value > 9:
                curval.right.value = Pair([Node(Number(math.floor(
                    curval.right.value.value / 2))), Node(Number(math.ceil(curval.right.value.value / 2)))])

                return pair, 2

        if isinstance(curval.left.value, Pair):
            stack.append(0)
            pair, action_type = reduce_pair_once(pair, stack)

            if action_type > 0:
                return pair, action_type

            stack.pop()

        if isinstance(curval.right.value, Pair):
            stack.append(1)
            pair, action_type = reduce_pair_once(pair, stack)

            if action_type > 0:
                return pair, action_type

            stack.pop()

    return pair, 0


def reduce_pair(pair):
    action_type = 1

    print(convert_pair(pair))

    while action_type > 0:
        pair, action_type = reduce_pair_once(pair, [])
        print(convert_pair(pair))

    return pair


def sum_sf_numbers(num1, num2):
    return "[" + num1 + "," + num2 + "]"


def sum_multi_sf_numbers(pairs):
    result = 0

    for pair in pairs:
        if result == 0:
            result = pair
        else:
            result = reduce_pair(sum_sf_numbers(result, pair))
            break

    return result


pairs = list(map(get_sf_numbers, input.splitlines()))
reduce_pair(pairs[0])
# print(convert_pair(pairs[0]))
