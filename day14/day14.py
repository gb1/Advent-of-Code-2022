from collections import namedtuple
from typing import Dict, List
import enum
from itertools import pairwise


class Material(enum.Enum):
    AIR = "."
    ROCK = "#"
    SAND = "~"


Point = namedtuple("Point", ("x", "y"))


def create_map() -> Dict[Point, Material]:
    wall_map = {}
    for x in range(490, 510):
        for y in range(10):
            wall_map[Point(x, y)] = Material.AIR
    return wall_map


def print_map(wall_map: Dict[Point, Material]) -> None:
    for y in range(10):
        print("")
        for x in range(490, 510):
            print(wall_map[(x, y)].value, end="")


def add_rocks(rocks: List[Point], wall_map: Dict[Point, Material]) -> Dict[Point, Material]:
    for rock in rocks:
        wall_map[rock] = Material.ROCK
    return wall_map


def create_rock_points(rocks: List[str]) -> List[Point]:
    points = []
    for rock_line in rocks:
        for rock in rock_line.split(" -> "):
            x, y = rock.split(", ")
            points.append(Point(int(x), int(y)))
    for start, end in pairwise(points):
        for x in range(start.x, end.x+1):
            for y in range(start.y, end.y+1):
                points.append(Point(x, y))

    return points


if __name__ == "__main__":
    rocks_lines = [
        "498, 4 -> 498, 6 -> 496, 6",
        # "503, 4 -> 502, 4 -> 502, 9 -> 494, 9"
    ]

    map = create_map()

    rock_points = create_rock_points(rocks_lines)

    map = add_rocks(rock_points, map)
    print_map(map)
