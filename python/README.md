# Python Assignments

## Overview
This repository contains small, focused Python assignments. Each problem lives in its own folder with a clear prompt, examples, and a test suite. Your job is to implement the functions in each `solution.py` file and then run the tests.

## Environment
- Python 3.11

## Install pytest
From the repository root:
```bash
docker run --rm -v "$PWD":/work -w /work python:3.11 bash -lc "pip install pytest && pytest -q"
```

## Dockerfile (optional)
Build once, then reuse:
```bash
docker build -t python-assignments .
docker run --rm -v "$PWD":/work -w /work python-assignments pytest -q
```

## Navigation
- `python/data_structures/` - search and validation problems (arrays, matrices, Sudoku)
- `python/concurrency/` - thread coordination, race conditions, and scheduling

## Suggested Order
1. data_structures/search_first_occurrence_k
2. data_structures/search_cyclically_sorted_array
3. data_structures/search_2d_sorted_array
4. data_structures/sudoku_checker_problem
5. concurrency/analyze_unsynchronized_threads
6. concurrency/sync_interleaving_threads
7. concurrency/timer_class

## Common pitfalls
- Skipping edge cases like empty inputs, single-element inputs, or missing targets.
- Assuming concurrency tests are deterministic; use proper synchronization and join threads.
- Forgetting to run tests from the correct directory or using the wrong Python version.

## No AI usage
Do not use AI assistants (Cursor/Claude/ChatGPT) to solve these problems. The goal is to build fundamentals: invariants, edge cases, and test-driven reasoning. AI-generated answers are often unreliable for concurrency, scheduling, and tricky edge cases.

## Optional background
If you want extra context for threading concepts, "Black Hat Python" is a useful optional background read.
