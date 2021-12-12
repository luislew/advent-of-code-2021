from day_10 import *

POINTS_MAP = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def find_completion_strings():
    for line in get_lines_from_input():
        result = check_line(line)
        if isinstance(result, list):
            # Generate the completion string from the open stack
            yield [OPEN_TO_CLOSE_MAP[char] for char in reversed(result)]


def get_score(completion_string):
    score = 0
    for char in completion_string:
        score *= 5
        score += POINTS_MAP[char]
    return score


if __name__ == "__main__":
    scores = sorted(get_score(completion_string) for completion_string in find_completion_strings())
    print(scores[(len(scores) - 1) // 2])
