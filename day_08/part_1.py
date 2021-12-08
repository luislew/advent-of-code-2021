from day_08 import get_digits_and_outputs, EASY_SEGMENT_LENGTHS_MAP


def count_easy_digits_in_outputs():
    return sum(
        1 for _, output in get_digits_and_outputs() for digit in output
        if len(digit) in EASY_SEGMENT_LENGTHS_MAP
    )


if __name__ == "__main__":
    print(count_easy_digits_in_outputs())
