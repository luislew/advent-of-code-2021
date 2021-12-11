from day_11 import Grid


def find_total_flashes():
    grid = Grid()
    for _ in range(100):
        grid.advance_state()
    return grid.flash_count


if __name__ == "__main__":
    print(find_total_flashes())
