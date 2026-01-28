from __future__ import annotations

from typing import List

import math

def is_valid_sudoku(board: List[List[int]]) -> bool:
    """Return True if a partial 9x9 Sudoku board is valid.

    Zeros represent blanks and are ignored in duplicate checks.
    """
    size = len(board)
    grid_size = int(math.sqrt(size))

    for row in range(0, size, grid_size):
        for col in range(0, size, grid_size):
            block = []

            for i in range(grid_size):
                block.extend(board[row + i][col: col + grid_size])

            if block and has_duplicates(block):
                return False

    return True

def has_duplicates(arr: List[int]) -> bool:
    values = [x for x in arr if x != 0]

    return len(values) != len(set(values))

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
