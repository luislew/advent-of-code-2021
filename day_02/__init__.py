import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_lines_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        return [line.strip() for line in f]
