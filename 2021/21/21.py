from itertools import product
from functools import cache

with open('21.in') as infile:
    input = infile.read()

lines = input.splitlines()
player1 = int(lines[0].split("Player 1 starting position: ")[1])
player2 = int(lines[1].split("Player 2 starting position: ")[1])


def deterministic_dice(count: int):
    return ((count * 3) % 100 + 1) + ((count * 3 + 1) % 100 + 1) + ((count * 3 + 2) % 100 + 1)


@cache
def calc_position(cur, die):
    return (cur + die + 9) % 10 + 1


def play_warm_up(player1, player2):
    score1 = 0
    score2 = 0
    count = 0

    while score1 < 1000 and score2 < 1000:
        if count % 2 == 0:
            player1 = calc_position(player1, deterministic_dice(count))
            score1 += player1
            count += 1
        else:
            player2 = calc_position(player2, deterministic_dice(count))
            score2 += player2
            count += 1

    return score1 if score1 < score2 else score2, count * 3


score, count = play_warm_up(player1, player2)
print(score, count, score * count)

possibles = [sum(c) for c in product(range(1, 4), repeat=3)]


@cache
def play(player1, score1, player2, score2, turn):
    if score1 >= 21:
        return 1, 0
    elif score2 >= 21:
        return 0, 1
    else:
        win1 = 0
        win2 = 0

        if turn == 0:
            for roll in possibles:
                w1, w2 = play(calc_position(player1, roll), score1 +
                              calc_position(player1, roll), player2, score2, 1)
                win1 += w1
                win2 += w2
        else:
            for roll in possibles:
                w1, w2 = play(player1, score1, calc_position(player2, roll),
                              score2 + calc_position(player2, roll), 0)
                win1 += w1
                win2 += w2

        return win1, win2


print(play(player1, 0, player2, 0, 0))
