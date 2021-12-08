from day_08 import get_digits_and_outputs, get_output_from_solved, solve_digits


def get_sum_of_outputs():
    return sum(
        get_output_from_solved(output, solve_digits(digits))
        for digits, output in get_digits_and_outputs()
    )


if __name__ == "__main__":
    print(get_sum_of_outputs())
