import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
#
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg
SEGMENTS_MAP = {
    0: {"a", "b", "c", "e", "f", "g"},
    1: {"c", "f"},
    2: {"a", "c", "d", "e", "g"},
    3: {"a", "c", "d", "f", "g"},
    4: {"b", "c", "d", "f"},
    5: {"a", "b", "d", "f", "g"},
    6: {"a", "b", "d", "e", "f", "g"},
    7: {"a", "c", "f"},
    8: {"a", "b", "c", "d", "e", "f", "g"},
    9: {"a", "b", "c", "d", "f", "g"},
}
EASY_DIGITS = {1, 4, 7, 8}
EASY_SEGMENT_LENGTHS_MAP = {len(SEGMENTS_MAP[d]): d for d in EASY_DIGITS}


def get_lines_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        for line in f:
            yield line.strip()


def get_digits_and_outputs():
    # Example line: daegb gadbcf cgefda edcfagb dfg acefbd fdgab fg bdcfa fcgb | cdfgba fgbc dbfac gfadbc
    for line in get_lines_from_input():
        digits_chunk, output_chunk = line.split(" | ")
        yield digits_chunk.split(), output_chunk.split()


def solve_digits(digits):
    # numeral -> digit
    solved = {}
    # orig segment -> new segment
    segment_map = {}

    # First, solve, the easy digits
    for digit in digits:
        segment_length = len(digit)
        if segment_length in EASY_SEGMENT_LENGTHS_MAP:
            solved[EASY_SEGMENT_LENGTHS_MAP[segment_length]] = set(digit)

    # Next, solve for remaining digits
    # Strategy:
    #   1. Divide into 5 and 6 char long groups
    #   2. Find unique characters within each group
    #   3. Map easy digits to original digit sets
    #   4. Find possible matches in unique characters
    #
    # 5 char digits: 2, 3, 5
    #   2 -> c, e
    #   3 -> c, f
    #   5 -> b, f
    # 6 char digits: 0, 6, 9
    #   0 -> c, e
    #   6 -> d, e
    #   9 -> c, d
    #
    # easy digits:
    #   1 -> c, f
    #   4 - 1 -> b, d
    #   7 - 1 -> a
    segment_map["a"] = list(solved[7] - solved[1])[0]

    for digit in digits:
        if len(digit) == 5 and set(digit).issuperset(solved[1]):
            solved[3] = set(digit)
            break

    segment_map["g"] = list(solved[3] - solved[4] - {segment_map["a"]})[0]

    # At this point, we know a, g and 1, 3, 4, 7, 8
    segment_map["e"] = list(solved[8] - solved[4] - solved[3])[0]
    # Now we know a, e, g and 1, 3, 4, 7, 8
    segment_map["b"] = list(solved[8] - solved[7] - solved[3] - {segment_map["e"]})[0]
    # Now we know a, b, e, g and 1, 3, 4, 7, 8
    for digit in digits:
        digit_set = set(digit)
        if len(digit) == 5:
            if segment_map["e"] in digit_set:
                solved[2] = digit_set
            elif segment_map["b"] in digit_set:
                solved[5] = digit_set
    # Now we know a, b, e, g and 1, 2, 3, 4, 5, 7, 8
    segment_map["c"] = list(solved[8] - solved[5] - {segment_map["e"]})[0]
    # Now we know a, b, c, e, g and 1, 2, 3, 4, 5, 7, 8
    for digit in digits:
        digit_set = set(digit)
        if len(digit) == 6:
            if segment_map["c"] not in digit_set:
                solved[6] = digit_set
            elif segment_map["e"] not in digit_set:
                solved[9] = digit_set
            else:
                solved[0] = digit_set

    return solved


def get_output_from_solved(output_digits, solved):
    output = []
    for digit in output_digits:
        digit_set = set(digit)
        for i, s in solved.items():
            if digit_set == s:
                output.append(i)
                break

    return int("".join(str(i) for i in output))
