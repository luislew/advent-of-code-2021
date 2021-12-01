from day_01 import get_depths_from_input


def depth_increases():
    depths = get_depths_from_input()
    last_depth = depths[0]
    increases = 0
    for depth in depths:
        if depth > last_depth:
            increases += 1
        last_depth = depth
    return increases


if __name__ == "__main__":
    print(depth_increases())
