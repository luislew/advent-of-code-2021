from day_03 import get_lines_from_input


def get_gamma_and_epsilon_rates():
    bit_counts_by_position = {}
    for line in get_lines_from_input():
        for i, char in enumerate(line):
            bit_counts_by_position.setdefault(i, {"0": 0, "1": 0})[char] += 1

    gamma_rate_str = ""
    epsilon_rate_str = ""
    for i, d in sorted(bit_counts_by_position.items()):
        zero_count = d["0"]
        one_count = d["1"]
        if zero_count > one_count:
            gamma_rate_str += "0"
            epsilon_rate_str += "1"
        else:
            gamma_rate_str += "1"
            epsilon_rate_str += "0"

    return int(gamma_rate_str, 2), int(epsilon_rate_str, 2)


if __name__ == "__main__":
    gamma_rate, epsilon_rate = get_gamma_and_epsilon_rates()
    print(gamma_rate * epsilon_rate)
