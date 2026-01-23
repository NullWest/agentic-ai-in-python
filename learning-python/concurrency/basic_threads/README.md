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

