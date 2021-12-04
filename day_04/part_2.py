from day_04 import find_number_on_board, get_numbers_and_boards, get_score, is_winning_board


def find_last_winning_board():
    numbers, boards = get_numbers_and_boards()
    marked_boards = [set() for _ in boards]
    winning_boards_idxs = []
    called_numbers = []
    for number in numbers:
        called_numbers.append(number)
        for idx, (board, marked_board) in enumerate(zip(boards, marked_boards)):
            if idx in winning_boards_idxs:
                continue

            match = find_number_on_board(board, number)
            if match:
                marked_board.add(match)
                if is_winning_board(marked_board):
                    winning_boards_idxs.append(idx)
                    if len(winning_boards_idxs) == len(boards):
                        return board, called_numbers


if __name__ == "__main__":
    board, called_numbers = find_last_winning_board()
    print(get_score(board, called_numbers))
