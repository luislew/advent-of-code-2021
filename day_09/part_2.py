from day_09 import Heightmap


def find_basin_for_coordinate(x, y, heightmap, visited, basin=None):
    basin = basin or set()
    point = (x, y)
    if point in visited:
        return basin

    visited.add(point)
    height = heightmap.get(x, y)
    if height == 9:
        return basin

    basin.add(point)
    for x_n, y_n in heightmap.get_neighbors(x, y):
        basin = find_basin_for_coordinate(x_n, y_n, heightmap, visited, basin)

    return basin


def find_basins():
    heightmap = Heightmap()
    visited = set()
    basins = []
    for y in range(heightmap.height):
        for x in range(heightmap.width):
            basin = find_basin_for_coordinate(x, y, heightmap, visited)
            if basin not in basins:
                basins.append(basin)

    return basins


if __name__ == "__main__":
    basins = find_basins()
    x, y, z = sorted(len(b) for b in basins)[-3:]
    print(x * y * z)
