import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_lines_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        for line in f:
            yield line.strip()


def get_initial_state():
    return [[int(c) for c in line] for line in get_lines_from_input()]


class Grid:
    def __init__(self):
        self.state = get_initial_state()
        self.height = len(self.state)
        self.width = len(self.state[0])
        self.flash_count = 0
        self.all_flashed = False

    def get(self, x, y):
        return self.state[y][x]

    def set(self, x, y, value):
        self.state[y][x] = value

    def increment(self, x, y):
        self.set(x, y, self.get(x, y) + 1)

    def get_neighbors(self, x, y):
        neighbors = [
            (x - 1, y - 1),
            (x, y - 1),
            (x + 1, y - 1),
            (x - 1, y),
            (x + 1, y),
            (x - 1, y + 1),
            (x, y + 1),
            (x + 1, y + 1),
        ]
        return [
            (x_n, y_n) for x_n, y_n in neighbors
            if 0 <= x_n < self.width and 0 <= y_n < self.height
        ]

    def increase_all_energies(self):
        for y in range(self.height):
            for x in range(self.width):
                self.increment(x, y)

    def flash(self):
        flashed = set()
        no_matches = False
        # Iteratively fire flashes and increment neighbors until we've fired all flashes
        while not no_matches:
            no_matches = True
            for y in range(self.height):
                for x in range(self.width):
                    point = (x, y)
                    if point in flashed:
                        continue

                    energy_level = self.get(x, y)
                    if energy_level < 10:
                        continue

                    # We found an octopus to flash
                    no_matches = False
                    flashed.add(point)
                    self.flash_count += 1
                    for x_n, y_n in self.get_neighbors(x, y):
                        self.increment(x_n, y_n)

        for x, y in flashed:
            self.set(x, y, 0)
        if len(flashed) == self.height * self.width:
            self.all_flashed = True

    def advance_state(self):
        self.increase_all_energies()
        self.flash()
