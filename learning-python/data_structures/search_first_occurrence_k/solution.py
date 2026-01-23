from __future__ import annotations

from typing import List


def search_first_occurrence(arr: List[int], k: int) -> int:
    """Return the first index of k in a sorted array with duplicates.

    Use a binary-search style approach. Return -1 if k is absent.
    """

    if len(arr) == 0:
        return -1

    left = 0
    right = len(arr) - 1
    last_found_index = -1

    while left <= right:
        middle = (left + right) // 2

        if arr[middle] == k:
            last_found_index = middle

            right = middle -1

            continue

        if arr[middle] < k:
            left = middle + 1
        else:
            right = middle - 1

    return last_found_index


if __name__ == "__main__":
    sample = [1, 2, 2, 2, 3]
    target = 2
    print("array:", sample)
    print("k:", target)

    print(search_first_occurrence(sample, target))
