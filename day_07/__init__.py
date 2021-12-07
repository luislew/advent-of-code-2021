import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_initial_state():
    with open(os.path.join(__location__, "input.txt")) as f:
        return [int(s) for s in f.read().strip().split(",")]


def get_fuel_usage_for_position(initial_state, position, fuel_usage_by_distance):
    return sum(fuel_usage_by_distance(abs(i - position)) for i in initial_state)


def get_minimum_fuel_usage(fuel_usage_by_distance):
    initial_state = get_initial_state()
    fuel_usage = None
    for position in range(min(initial_state), max(initial_state) + 1):
        fuel_for_position = get_fuel_usage_for_position(initial_state, position, fuel_usage_by_distance)
        if fuel_usage is None or fuel_for_position < fuel_usage:
            fuel_usage = fuel_for_position

    return fuel_usage
