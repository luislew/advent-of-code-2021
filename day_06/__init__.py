import os
from collections import Counter

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_initial_state():
    with open(os.path.join(__location__, "input.txt")) as f:
        return [int(s) for s in f.read().strip().split(",")]


def simulate_days(days):
    state = get_initial_state()
    counter = Counter(state)
    for _ in range(days):
        new_counter = Counter()
        new_fish = 0
        for interval, count in counter.items():
            if interval == 0:
                new_counter[6] += count
                new_fish = count
            else:
                new_counter[interval - 1] += count
        new_counter[8] = new_fish
        counter = new_counter

    return counter
