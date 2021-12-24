from itertools import cycle

from day_21 import *


def die():
    return cycle(range(1, 1001))


def play_game():
    turn = 0
    position_1, position_2 = get_starting_positions()
    score_1, score_2 = 0, 0
    roller = die()
    while score_1 < 1000 and score_2 < 1000:
        turn += 1
        total_roll = 0
        for _ in range(3):
            total_roll += next(roller)
        if turn % 2:
            position_1, score_1 = get_new_position_and_score(position_1, score_1, total_roll)
        else:
            position_2, score_2 = get_new_position_and_score(position_2, score_2, total_roll)

    return score_1, score_2, turn * 3


if __name__ == "__main__":
    score_1, score_2, rolls = play_game()
    losing_score = min(score_1, score_2)
    print(losing_score * rolls)
