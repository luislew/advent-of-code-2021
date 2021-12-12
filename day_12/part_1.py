from day_12 import CaveMap


if __name__ == "__main__":
    cave_map = CaveMap()
    print(len(cave_map.find_paths(CaveMap.START)))
