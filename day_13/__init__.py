import os
from typing import List, Set, Tuple

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_lines_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        for line in f:
            yield line.strip()


class PaperGrid:
    def __init__(self):
        self.dots: Set[Tuple[int, int]] = set()
        self.folds: List[Tuple[str, int]] = []

        for line in get_lines_from_input():
            if line.startswith("fold"):
                fold_spec = line.rsplit(" ", 1)[-1]
                axis, val_str = fold_spec.split("=")
                self.folds.append((axis, int(val_str)))
            elif line:
                x_str, y_str = line.split(",")
                self.dots.add((int(x_str), int(y_str)))

    def fold(self):
        axis, value = self.folds.pop(0)
        elem = 0 if axis == "x" else 1
        new_dots = set()
        for dot in self.dots:
            x, y = dot
            if dot[elem] > value:
                new_dots.add((x, 2 * value - y) if elem else (2 * value - x, y))
            else:
                new_dots.add(dot)
        self.dots = new_dots

    def render(self):
        max_x = max_y = 0
        for x, y in self.dots:
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y

        for y in range(max_y + 1):
            print("".join("█" if (x, y) in self.dots else " " for x in range(max_x + 1)))
