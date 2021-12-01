from day_01 import get_depths_from_input


def depth_window_increases():
    depths = get_depths_from_input()
    last_window = sum(depths[:3])
    increases = 0
    for i in range(len(depths) - 2):
        window = sum(depths[i:i + 3])
        if window > last_window:
            increases += 1
        last_window = window
    return increases


if __name__ == "__main__":
    print(depth_window_increases())
