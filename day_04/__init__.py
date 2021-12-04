import os
from itertools import chain

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

WINNING_COMBOS = [
    # Diagonals
    {(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)},
    {(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)},
]
# Columns
for x in range(5):
    WINNING_COMBOS.append({(x, y) for y in range(5)})
# Rows
for y in range(5):
    WINNING_COMBOS.append({(x, y) for x in range(5)})


def get_lines_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        return [line.strip() for line in f]


def get_numbers_and_boards():
    numbers = None
    current_board = None
    boards = []
    for line in get_lines_from_input():
        if numbers is None:
            numbers = [int(s) for s in line.split(",")]
            continue

        if not line:
            if current_board:
                boards.append(current_board)
            current_board = []
            continue

        current_board.append([int(s) for s in line.split()])

    if current_board:
        boards.append(current_board)

    return numbers, boards


def find_number_on_board(board, number):
    for y, row in enumerate(board):
        try:
            x = row.index(number)
        except ValueError:
            continue
        else:
            return x, y


def is_winning_board(marked_board):
    # Look for a row, column, or diagonal in marked (x, y) pairs
    if len(marked_board) < 5:
        return False

    return any(marked_board.issuperset(combo) for combo in WINNING_COMBOS)


def get_score(winning_board, called_numbers):
    sum_unmarked_numbers = sum(i for i in chain.from_iterable(winning_board) if i not in called_numbers)
    return sum_unmarked_numbers * called_numbers[-1]
