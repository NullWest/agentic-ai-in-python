from __future__ import annotations

from typing import List

def is_valid_sudoku(board: List[List[int]]) -> bool:
    """Return True if a partial 9x9 Sudoku board is valid.

    Zeros represent blanks and are ignored in duplicate checks.
    """

    is_valid = True
    grid_quantity = 3
    board_length = len(board)

    for index in range(board_length):
        position = index * grid_quantity if index > 0 else index

        if position >= board_length:
            break

        row = board[position]
        second_row = board[position + 1]
        third_row = board[position + 2]

        start = 0
        end = 3

        for _ in row:
            top = row[start:end]
            middle = second_row[start:end]
            bottom = third_row[start:end]

            if has_duplicates(top + middle + bottom):
                return False

            start += grid_quantity
            end += grid_quantity

    return is_valid

def ignore_zeros(arr: List[int]) -> List[int]:
    return list(filter(lambda digit: digit != 0, arr))

def has_duplicates(arr: List[int]) -> bool:
    list_without_zeros = ignore_zeros(arr)

    return len(list_without_zeros) != len(set(list_without_zeros))

if __name__ == "__main__":
    sample = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    print("valid:", is_valid_sudoku(sample))
