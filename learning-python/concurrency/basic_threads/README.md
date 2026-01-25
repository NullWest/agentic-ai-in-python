# Coding Challenge: Concurrent File System Tree Printer

## Summary
Build a command-line program that prints a readable “tree view” of a directory, similar to the Unix `tree` command. The twist: your traversal must use **threads** to explore subfolders concurrently.

This challenge is designed to assess correctness, clarity, and pragmatic concurrency decisions.

---

## Requirements

### Core Behavior
- Given a starting directory path, print a directory tree to stdout.
- Directories must be visually distinguished (e.g., trailing `/`).
- Indentation must reflect nesting depth.

### Concurrency
- Your program must use **threads** to traverse the file system.
- When encountering a directory, your implementation should be able to **branch out** to process different subdirectories concurrently.
- Thread creation and coordination must be safe and bounded (i.e., avoid unbounded thread spawning on large trees).

### Determinism
- Output must be **deterministic** for the same directory contents.
- You may choose an ordering rule (e.g., lexical sort), but it must be consistent.

### Correctness Constraints
- Do not crash on:
  - Empty directories
  - Deep nesting
  - Permission errors (handle gracefully)
- Avoid infinite recursion on systems where symlinks could create cycles (you may choose a policy regarding symlinks, but document it).

---

## Input / Invocation
Your program should be runnable as one of the following (choose one and document it):

- `python tree_threads.py /path/to/root`
- or `python -m tree_threads /path/to/root`

Optional flags are allowed (depth limit, include hidden files, follow symlinks), but not required.

---

## Output Format
Your output should resemble:

root/
README.md
src/
main.py
utils/
helpers.py
tests/
test_main.py


Notes:
- The exact indentation characters are up to you, but must be consistent.
- You should not print duplicate entries.
- If a directory cannot be read, print a single line indicating it was skipped (exact wording is up to you).

---

## Performance Expectations
- The program should complete quickly on moderate directory sizes.
- Concurrency should not degrade performance or overwhelm the system.
- Avoid excessive memory usage.

---

## Evaluation Criteria
You will be evaluated on:
1. Correctness of the printed tree
2. Deterministic ordering
3. Soundness of the threading model (bounded, safe, clean shutdown)
4. Error handling and resilience
5. Code readability and structure

---

## Deliverables
Submit:
- Source code
- A short `README` explaining:
  - How to run it
  - Your deterministic ordering rule
  - Your policy on symlinks
  - How you bounded / managed threading

---

## Rules
- Use the standard library only.
- Do not shell out to `tree` or other external tools.
- Keep it simple and robust.

---

## Optional Extensions (only if you finish early)
Pick at most one:
- Max depth flag
- “Only directories” mode
- Include/exclude patterns (glob)
- Summary line (total files/dirs)

---

# Directory Tree (Python)

A simple Python command-line tool that displays a directory tree structure, similar to the Unix `tree` command.  
It recursively scans directories and prints their hierarchy in a readable, indented format.

This project was created as a learning exercise focused on filesystem traversal, concurrency, and command-line interface design in Python.

---

## Features

- Recursively displays directory structures
- Optional flag to display **only directories**
- Sorted output for deterministic and readable results using lexical sorting
- Uses `os.scandir` for efficient filesystem access
- Concurrent directory traversal using `ThreadPoolExecutor`
- Uses only Python’s standard library

---

## Requirements

- Python 3.9

---

## Usage

Run the script from the command line:

```bash
python solution.py <path>
```

Example Output:

```bash
README.md
example/
  a/
  b/
    bb/
  c/
    cc/
solution.py
```

### Available flags:

--only-directories: Only display directories

```bash
python solution.py <path> --only-directories
```

Example Output:

```bash
example/
  a/
  b/
    bb/
  c/
    cc/
```

---

## Concurrency Model

- Directory scanning is performed using a ThreadPoolExecutor.
- Threads are used only during the directory-reading phase.
- The program waits for all submitted tasks to finish before printing.
Output is generated in a single thread to ensure deterministic ordering.

Note: Threading is used mainly for educational purposes. For small directory trees, 
threading may not provide performance benefits due to overhead.

---

## Limitations

---

1. Symbolic links are ignored to prevent infinite recursion.
2. Large directory trees may consume significant memory.
3. Threading overhead may outweigh performance gains for small inputs.