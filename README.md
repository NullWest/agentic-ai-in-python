# Python Assignments

## Overview
This is a series of small Python assignments intended to help software developers unfamiliar with python practice some of the key challenges that will occur in later Agentic AI development.
The first series "data_structures" focuses on sorting and searching arrays.  The second is centered around data streams and parallel processing.

Each problem lives in its own folder containing the instructions in a README.md, a test suite, and a template solutions file. Your job is to implement the functions in each `solution.py` file and then run the tests.

## Docker

We recommend using Docker for your agentic AI projects. Docker for provides a controlled, isolated runtime that encapsulates the Python interpreter, system libraries, and all application dependencies into a single, predictable environment. Python packages often rely on native system components (such as SSL libraries, image codecs, or database drivers) that can behave differently across operating systems or even across machines running the same OS. Docker eliminates this variability by ensuring the same versions of Python, OS-level dependencies, and packages are used everywhere. This isolation also protects the host system by preventing dependency conflicts, reducing the risk of accidental system-level changes, and allowing developers to experiment or upgrade libraries without impacting other projects or the underlying machine


## Dockerfile
To build Docker for the first time, run the following on the root directory:
```bash
docker build -t python-assignments .
```

The specific commands for running Docker within the directory are listed on each README.


## Suggested Assignment Order
1. data_structures/sudoku_checker_problem
1. data_structures/search_first_occurrence_k
1. data_structures/search_cyclically_sorted_array
1. data_structures/search_2d_sorted_array
1. concurrency/analyze_unsynchronized_threads
1. concurrency/sync_interleaving_threads
1. concurrency/timer_class

## No AI usage
Do not use AI assistants (Cursor/Claude/ChatGPT) to solve these problems. The goal is to build fundamentals: invariants, edge cases, and test-driven reasoning. AI-generated answers are often unreliable for concurrency, scheduling, and tricky edge cases.

