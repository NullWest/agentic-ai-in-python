# sudoku_checker_problem

## What you are building
Write a function that validates a partially filled 9x9 Sudoku board. The board is valid if:
- Each row contains no duplicate digits 1-9.
- Each column contains no duplicate digits 1-9.
- Each 3x3 subgrid contains no duplicate digits 1-9.
- The value `0` represents an empty cell and should be ignored during checks.

This is not a solver. You are only checking whether the current state is valid.

## Input / Output + Constraints
- Input: `board: list[list[int]]` a 9x9 grid containing values 0-9
- Output: `bool` `True` if valid so far, otherwise `False`
- Constraint: ignore zeros; validate rows, columns, and 3x3 subgrids

## Examples
- A valid partial board -> `True`
- A row with two `5` values -> `False`
- A column with two `9` values -> `False`

## Common pitfalls
- Treating zeros as normal digits rather than blanks.
- Forgetting to reset tracking for each row, column, or subgrid.
- Mixing up subgrid boundaries (use 3x3 blocks).

## Getting Started
- Implement `is_valid_sudoku(board)` in `solution.py`.
- First time: from the repo root, build the image: `docker build -t python-assignments .`
- Run tests (Docker): `docker run --rm -v "$PWD":/work -w /work python-assignments pytest -q tests.py`
- Fallback (Docker): `docker run --rm -v "$PWD":/work -w /work python-assignments python tests.py`
