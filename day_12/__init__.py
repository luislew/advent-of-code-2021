import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

from typing import List, Optional, Tuple


def get_lines_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        for line in f:
            yield line.strip()


class CaveMap:
    START = "start"
    END = "end"

    def __init__(self):
        self.map = {}
        for line in get_lines_from_input():
            node1, node2 = line.split("-")
            self.map.setdefault(node1, set()).add(node2)
            self.map.setdefault(node2, set()).add(node1)

    @staticmethod
    def is_large_cave(node: str):
        return node.isupper()

    @staticmethod
    def is_small_cave(node: str):
        return node.islower() and len(node) == 2

    def has_no_duplicate_small_caves(self, current_path: Tuple[str]):
        seen = set()
        for node in current_path:
            if self.is_small_cave(node):
                if node in seen:
                    return False
                seen.add(node)

        return True

    def is_eligible_node(self, node: str, current_path: Tuple[str], allow_extra_small_cave_visit: bool):
        if self.is_large_cave(node):
            return True
        elif self.is_small_cave(node):
            if node not in current_path:
                return True
            elif allow_extra_small_cave_visit and self.has_no_duplicate_small_caves(current_path):
                return True
        elif node == self.END:
            return True
        return False

    def find_paths(
        self,
        start: str,
        current_path: Optional[Tuple[str]] = None,
        paths: Optional[List[Tuple[str]]] = None,
        allow_extra_small_cave_visit: bool = False,
    ):
        if paths is None:
            paths = []
        if current_path is None:
            current_path = (start,)

        for adjacent_node in self.map[start]:
            if self.is_eligible_node(adjacent_node, current_path, allow_extra_small_cave_visit):
                new_path = current_path + (adjacent_node,)
                if adjacent_node == self.END:
                    paths.append(new_path)
                else:
                    self.find_paths(adjacent_node, new_path, paths, allow_extra_small_cave_visit)

        return paths
