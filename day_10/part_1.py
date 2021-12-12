from day_10 import *

POINTS_MAP = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def find_first_illegal_characters():
    for line in get_lines_from_input():
        result = check_line(line)
        if isinstance(result, str):
            yield result


if __name__ == "__main__":
    print(sum(POINTS_MAP[char] for char in find_first_illegal_characters()))
