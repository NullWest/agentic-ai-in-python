from __future__ import annotations

from typing import List


def is_valid_sudoku(board: List[List[int]]) -> bool:
    """Return True if a partial 9x9 Sudoku board is valid.

    Zeros represent blanks and are ignored in duplicate checks.
    """
    if len(board) != 9:
        return False
    for row in board:
        if len(row) != 9:
            return False

    def valid_group(values: List[int]) -> bool:
        seen = set()
        for value in values:
            if value == 0:
                continue
            if value < 1 or value > 9:
                return False
            if value in seen:
                return False
            seen.add(value)
        return True

    for row in board:
        if not valid_group(row):
            return False

    for col in range(9):
        column_vals = [board[row][col] for row in range(9)]
        if not valid_group(column_vals):
            return False

    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            block = []
            for r in range(box_row, box_row + 3):
                for c in range(box_col, box_col + 3):
                    block.append(board[r][c])
            if not valid_group(block):
                return False

    return True


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
