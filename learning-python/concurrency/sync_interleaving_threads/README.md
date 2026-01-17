# sync_interleaving_threads

## What you are building
Write a function that runs two threads: one emits odd numbers and the other emits even numbers. The combined output must be a single ordered list from 1 to `limit` with no gaps or reordering.

The main challenge is synchronization. Even though two threads are running, the final sequence must be strictly ordered.

## Input / Output + Constraints
- Input: optional `limit` (default 100)
- Output: ordered list of integers from 1..limit
- Constraint: use synchronization so the sequence is ordered even with concurrency

## Examples
- `limit=5 -> [1,2,3,4,5]`
- `limit=1 -> [1]`
- `limit=2 -> [1,2]`

## Common pitfalls
- Appending out of order because the threads race.
- Missing the last number due to incorrect loop bounds.
- Forgetting to join threads before returning the output.

## Getting Started
- Implement `run_ordered_printer(limit=100)` in `solution.py`.
- First time: from the repo root, build the image: `docker build -t python-assignments .`
- Run tests (Docker): `docker run --rm -v "$PWD":/work -w /work python-assignments pytest -q tests.py`
- Fallback (Docker): `docker run --rm -v "$PWD":/work -w /work python-assignments python tests.py`
