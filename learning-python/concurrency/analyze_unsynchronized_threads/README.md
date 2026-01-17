# analyze_unsynchronized_threads

## What you are building
Create helper functions that simulate two unsynchronized threads modifying shared state. You will enumerate or sample all valid interleavings and then analyze the possible final outcomes. The goal is to show how race conditions arise from different schedules.

Think of each thread as a list of steps (like `read`, `inc`, `write`). Interleavings must preserve the order of steps within each thread.

## Input / Output + Constraints
- Input: step lists for thread A and thread B
- Output: interleavings and a set of possible final shared values
- Constraint: preserve each thread's step order in any interleaving

## Examples
- `A=[read,inc,write], B=[read,inc,write] -> possible finals {1,2}`
- `A=[read,write], B=[read,write] -> possible finals {0}`
- `A=[], B=[read] -> possible finals {0}`

## Common pitfalls
- Generating interleavings that violate the per-thread step order.
- Forgetting that the local register and shared value are different.
- Assuming one deterministic outcome rather than a set of outcomes.

## Getting Started
- Implement the helpers in `solution.py`.
- First time: from the repo root, build the image: `docker build -t python-assignments .`
- Run tests (Docker): `docker run --rm -v "$PWD":/work -w /work python-assignments pytest -q tests.py`
- Fallback (Docker): `docker run --rm -v "$PWD":/work -w /work python-assignments python tests.py`
