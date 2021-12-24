import functools
from pathlib import Path

__location__ = Path(__file__).parent


def get_lines_from_input():
    input_file = Path(__file__).parent / "input.txt"
    with input_file.open() as f:
        for line in f:
            yield line.strip()


def get_starting_positions():
    return [int(line.split(": ")[-1]) for line in get_lines_from_input()]


@functools.lru_cache()
def get_position_for_roll(start_position, roll):
    position = start_position + roll
    return (position % 10) or 10


def get_new_position_and_score(position, score, roll):
    new_position = get_position_for_roll(position, roll)
    new_score = score + new_position
    return new_position, new_score
