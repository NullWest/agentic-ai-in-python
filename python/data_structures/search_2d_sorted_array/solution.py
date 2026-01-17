from __future__ import annotations

from typing import List, Optional, Tuple


def search_2d_sorted(matrix: List[List[int]], k: int) -> Optional[Tuple[int, int]]:
    """Return (row, col) if k is in the sorted matrix, else None.

    Each row is sorted left-to-right and each column is sorted top-to-bottom.
    """
    # TODO: implement a linear-time (m + n) search
    raise NotImplementedError


if __name__ == "__main__":
    sample = [
        [1, 4, 7],
        [2, 5, 9],
        [3, 6, 10],
    ]
    target = 5
    print("matrix:", sample)
    print("k:", target)
    # TODO: call search_2d_sorted and print the result
