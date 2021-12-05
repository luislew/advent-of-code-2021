import os
from collections import Counter

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_lines_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        return [line.strip() for line in f]


def get_line_segments():
    for line in get_lines_from_input():
        p1, p2 = line.split(" -> ")
        point1 = tuple(int(s) for s in p1.split(","))
        point2 = tuple(int(s) for s in p2.split(","))
        yield point1, point2


def count_overlaps(include_diagonals=False):
    counter = Counter()
    for point1, point2 in get_line_segments():
        (x1, y1), (x2, y2) = point1, point2
        if x1 == x2:
            y_start, y_stop = (y1, y2) if y2 > y1 else (y2, y1)
            for y in range(y_start, y_stop + 1):
                counter[(x1, y)] += 1
        elif y1 == y2:
            x_start, x_stop = (x1, x2) if x2 > x1 else (x2, x1)
            for x in range(x_start, x_stop + 1):
                counter[(x, y1)] += 1
        elif include_diagonals:
            (x_start, y_start), (x_stop, y_stop) = (point1, point2) if x2 > x1 else (point2, point1)
            distance = x_stop - x_start
            for i in range(distance + 1):
                point = (x_start + i, y_start + i if y_start < y_stop else y_start - i)
                counter[point] += 1

    return sum(1 for count in counter.values() if count > 1)
