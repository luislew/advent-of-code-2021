from day_11 import Grid


def find_simultaneous_flash_step():
    grid = Grid()
    step = 0
    while not grid.all_flashed:
        step += 1
        grid.advance_state()
    return step


if __name__ == "__main__":
    print(find_simultaneous_flash_step())
