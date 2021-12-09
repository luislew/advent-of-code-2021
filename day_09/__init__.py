import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_lines_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        for line in f:
            yield line.strip()


def get_heightmap_and_dimensions():
    heightmap = [[int(c) for c in line] for line in get_lines_from_input()]
    map_height = len(heightmap)
    map_width = len(heightmap[0])
    return heightmap, map_height, map_width


class Heightmap:
    def __init__(self):
        self.map, self.height, self.width = get_heightmap_and_dimensions()

    def get(self, x, y):
        return self.map[y][x]

    def get_neighbors(self, x, y):
        neighbors = [
            (x, y + 1),
            (x, y - 1),
            (x + 1, y),
            (x - 1, y),
        ]
        return [
            (x_n, y_n) for x_n, y_n in neighbors
            if 0 <= x_n < self.width and 0 <= y_n < self.height
        ]
