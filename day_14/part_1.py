from day_14 import Polymer


if __name__ == "__main__":
    polymer = Polymer()
    for _ in range(10):
        polymer.do_pair_insertions()
    most_common_count, least_common_count = polymer.get_most_least_common_character_counts()
    print(most_common_count - least_common_count)
