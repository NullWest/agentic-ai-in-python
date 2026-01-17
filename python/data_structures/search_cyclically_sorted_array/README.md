# search_cyclically_sorted_array

## What you are building
Write a function that finds the index of `k` in a cyclically (rotated) sorted array of distinct integers. If `k` is not present, return `-1`.

The array was originally sorted, then rotated at some pivot. You should use a modified binary search to achieve logarithmic time.

## Input / Output + Constraints
- Input: `arr: list[int]` rotated sorted array with distinct values; `k: int`
- Output: `int` index of `k`, or `-1` if missing
- Constraint: aim for `O(log n)` time

## Examples
- `arr=[4,5,6,1,2,3], k=2 -> 4`
- `arr=[30,40,50,5,10,20], k=5 -> 3`
- `arr=[1,2,3], k=9 -> -1`

## Common pitfalls
- Mishandling the pivot when the target lies in the other half.
- Forgetting that values are distinct (no duplicates to complicate comparisons).
- Off-by-one errors when moving the low/high pointers.

## Getting Started
- Implement `search_cyclically_sorted(arr, k)` in `solution.py`.
- First time: from the repo root, build the image: `docker build -t python-assignments .`
- Run tests (Docker): `docker run --rm -v "$PWD":/work -w /work python-assignments pytest -q tests.py`
- Fallback (Docker): `docker run --rm -v "$PWD":/work -w /work python-assignments python tests.py`
