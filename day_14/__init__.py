import os
from collections import Counter
from typing import Dict, Optional, Tuple

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_lines_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        for line in f:
            yield line.strip()


class Polymer:
    def __init__(self):
        self.pairs_counter: Optional[Counter] = None
        self.pairs_map: Dict[Tuple[str, str], str] = {}
        self.chain_start: Optional[str] = None
        self.chain_end: Optional[str] = None
        for line in get_lines_from_input():
            if self.pairs_counter is None:
                # Populate the pairs counter
                self.chain_start = line[0]
                self.chain_end = line[-1]
                self.pairs_counter = Counter((i, j) for i, j in zip(line, line[1:]))
            elif line:
                pair, char = line.split(" -> ")
                self.pairs_map[tuple(pair)] = char

    def do_pair_insertions(self):
        insert_counter = Counter()
        for pair, count in self.pairs_counter.items():
            # Given: AB -> C and chain of AB
            # AC += 1, BC += 1, AB -= 1
            i, j = pair
            insert_char = self.pairs_map[pair]
            insert_counter[(i, insert_char)] += count
            insert_counter[(insert_char, j)] += count
            insert_counter[pair] -= count
        self.pairs_counter += insert_counter

    def get_most_least_common_character_counts(self) -> Tuple[int, int]:
        # Given original pairs of AB, BC, CD, the actual character counts
        # will be the total counts divided by two, *except* that we need to
        # adjust up 0.5 for the start and end character
        char_counter = Counter({self.chain_start: 1, self.chain_end: 1})
        for (i, j), count in self.pairs_counter.items():
            char_counter[i] += count
            char_counter[j] += count
        most_common_chars = char_counter.most_common()
        return most_common_chars[0][1] // 2, most_common_chars[-1][1] // 2
