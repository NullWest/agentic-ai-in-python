# search_first_occurrence_k

## What you are building
Write a function that finds the first position of a target value `k` in a sorted list that may contain duplicates. If the value does not appear, return `-1`.

This is a classic binary-search variation. A linear scan is too slow for large inputs, so the expected solution should be better than `O(n)`.

## Input / Output + Constraints
- Input: `arr: list[int]` sorted in non-decreasing order, may contain duplicates; `k: int`
- Output: `int` index of the first occurrence of `k`, or `-1` if missing
- Constraint: aim for `O(log n)` time

## Examples
- `arr=[1,2,2,2,3], k=2 -> 1` (first 2 is at index 1)
- `arr=[1,3,5], k=4 -> -1` (missing)
- `arr=[], k=7 -> -1` (empty array)

## Common pitfalls
- Returning any occurrence instead of the first one.
- Off-by-one mistakes when shrinking the binary search window.
- Not handling empty arrays or all-duplicate arrays correctly.

## Getting Started
- Implement `search_first_occurrence(arr, k)` in `solution.py`.
- First time: from the repo root, build the image: `docker build -t python-assignments .`
- Run tests (Docker): `docker run --rm -v "$PWD":/work -w /work python-assignments pytest -q tests.py`
- Fallback (Docker): `docker run --rm -v "$PWD":/work -w /work python-assignments python tests.py`
