from __future__ import annotations

from typing import List, Optional, Tuple


def search_2d_sorted(matrix: List[List[int]], k: int) -> Optional[Tuple[int, int]]:
    """Return (row, col) if k is in the sorted matrix, else None.

    Each row is sorted left-to-right and each column is sorted top-to-bottom.
    """

    if not matrix:
        return None

    row = 0
    col = len(matrix[0]) - 1
    row_limit = len(matrix) - 1

    while matrix[row][col] != k:
        if matrix[row][col] == k:
            return row, col

        if matrix[row][col] > k:
            col -= 1
        else:
            if row == row_limit:
                return None

            current_row_length = len(matrix[row])
            next_row_length = len(matrix[row + 1])

            if next_row_length < current_row_length:
                col -= 1

            row += 1

    return row, col

if __name__ == "__main__":
    sample = [
        [1, 4, 7],
        [2, 5, 9],
        [3, 6, 10],
    ]
    target = 5
    print("matrix:", sample)
    print("k:", target)
