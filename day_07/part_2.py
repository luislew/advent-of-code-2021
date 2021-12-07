from day_07 import get_minimum_fuel_usage


if __name__ == "__main__":
    print(get_minimum_fuel_usage(lambda d: int((d + 1) * d / 2)))
