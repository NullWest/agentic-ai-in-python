from __future__ import annotations

from typing import List


def search_cyclically_sorted(arr: List[int], k: int) -> int:
    """Return the index of k in a rotated sorted array of distinct ints.

    Return -1 if k is absent. Aim for logarithmic time.
    """

    if not arr:
        return -1

    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        if arr[middle] == k:
            return middle

        is_left_sort = arr[left] <= arr[middle]

        if is_left_sort:
           target_is_in_left_half = arr[left] <= k <= arr[middle]

           if target_is_in_left_half:
               right = middle - 1
           else:
               left = middle + 1

        else:
            target_is_in_right_half = arr[middle] <= k <= arr[right]

            if target_is_in_right_half:
                left = middle + 1
            else:
                right = middle - 1

    return -1


if __name__ == "__main__":
    sample = [4, 5, 6, 1, 2, 3]
    target = 2
    print("array:", sample)
    print("k:", target)
    print( search_cyclically_sorted(sample, target))
