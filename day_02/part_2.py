from day_02 import get_lines_from_input


def solution():
    aim = 0
    x = 0
    z = 0
    for line in get_lines_from_input():
        direction, magnitude_str = line.split()
        magnitude = int(magnitude_str)
        if direction == "forward":
            x += magnitude
            z += aim * magnitude
        elif direction == "up":
            aim -= magnitude
        elif direction == "down":
            aim += magnitude
    return x, z


if __name__ == "__main__":
    x, z = solution()
    print(x * z)
