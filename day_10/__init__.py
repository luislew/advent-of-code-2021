import os
from typing import Union

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

OPEN_TO_CLOSE_MAP = {"(": ")", "[": "]", "{": "}", "<": ">"}
OPEN_CHARS = set(OPEN_TO_CLOSE_MAP)
CLOSE_CHARS = set(OPEN_TO_CLOSE_MAP.values())


def get_lines_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        for line in f:
            yield line.strip()


def check_line(line) -> Union[str, list]:
    """Return illegal char if invalid, or open stack if incomplete"""
    stack = []
    for char in line:
        if char in OPEN_CHARS:
            stack.append(char)
        else:
            expected_char = OPEN_TO_CLOSE_MAP[stack[-1]]
            if char == expected_char:
                stack.pop()
            else:
                return char

    return stack
