from day_09 import Heightmap


def find_low_points():
    heightmap = Heightmap()
    for y in range(heightmap.height):
        for x in range(heightmap.width):
            # Test for low point
            height = heightmap.get(x, y)
            is_low_point = all(
                height < heightmap.get(x_n, y_n)
                for x_n, y_n in heightmap.get_neighbors(x, y)
            )
            if is_low_point:
                yield height


if __name__ == "__main__":
    low_points = find_low_points()
    print(sum(i + 1 for i in low_points))
