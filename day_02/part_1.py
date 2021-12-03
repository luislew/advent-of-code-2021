from day_02 import get_lines_from_input


def solution():
    x = 0
    z = 0
    for line in get_lines_from_input():
        direction, magnitude_str = line.split()
        magnitude = int(magnitude_str)
        if direction == "forward":
            x += magnitude
        elif direction == "up":
            z -= magnitude
        elif direction == "down":
            z += magnitude
    return x, z


if __name__ == "__main__":
    x, z = solution()
    print(x * z)
