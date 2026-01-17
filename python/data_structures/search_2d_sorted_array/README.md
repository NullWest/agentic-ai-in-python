# search_2d_sorted_array

## What you are building
Write a function that searches a 2D matrix where each row is sorted left-to-right and each column is sorted top-to-bottom. If the target value is found, return its `(row, col)` position. If it is not found, return `None`.

A common approach starts from the top-right (or bottom-left) and walks across the matrix in `O(m + n)` time.

## Input / Output + Constraints
- Input: `matrix: list[list[int]]` with sorted rows and columns; `k: int`
- Output: `(row, col)` tuple if found, otherwise `None`
- Constraint: aim for `O(m + n)` time

## Examples
- `matrix=[[1,4,7],[2,5,9],[3,6,10]], k=5 -> (1,1)`
- `matrix=[[1,2],[3,4]], k=8 -> None`
- `matrix=[], k=1 -> None`

## Common pitfalls
- Starting in the wrong corner and moving in the wrong direction.
- Returning `(col, row)` instead of `(row, col)`.
- Not handling empty matrices or empty rows.

## Getting Started
- Implement `search_2d_sorted(matrix, k)` in `solution.py`.
- First time: from the repo root, build the image: `docker build -t python-assignments .`
- Run tests (Docker): `docker run --rm -v "$PWD":/work -w /work python-assignments pytest -q tests.py`
- Fallback (Docker): `docker run --rm -v "$PWD":/work -w /work python-assignments python tests.py`
