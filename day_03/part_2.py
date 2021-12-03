from day_03 import get_lines_from_input


def get_rating(bit_criteria, lines=None, idx=0):
    if lines is None:
        lines = get_lines_from_input()

    zeroes, ones = [], []
    for line in lines:
        zeroes.append(line) if line[idx] == "0" else ones.append(line)

    candidates = bit_criteria(zeroes, ones)
    if len(candidates) == 1:
        return int(candidates[0], 2)
    else:
        return get_rating(bit_criteria, lines=candidates, idx=idx + 1)


def get_oxygen_generator_rating():
    return get_rating(lambda zeroes, ones: zeroes if len(zeroes) > len(ones) else ones)


def get_co2_scrubber_rating():
    return get_rating(lambda zeroes, ones: ones if len(ones) < len(zeroes) else zeroes)


if __name__ == "__main__":
    oxygen_generator_rating = get_oxygen_generator_rating()
    co2_scrubber_rating = get_co2_scrubber_rating()
    print(oxygen_generator_rating * co2_scrubber_rating)
