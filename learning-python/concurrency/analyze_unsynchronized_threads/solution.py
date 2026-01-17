from __future__ import annotations

import random
from typing import Iterable, List, Sequence, Set, Tuple


Step = str


def enumerate_interleavings(steps_a: Sequence[Step], steps_b: Sequence[Step]) -> List[List[Tuple[str, Step]]]:
    """Return all valid interleavings of two step lists.

    Each output sequence contains tagged steps: ("A", step) or ("B", step).
    The relative order of steps within each thread must be preserved.
    """
    results: List[List[Tuple[str, Step]]] = []

    def backtrack(i: int, j: int, current: List[Tuple[str, Step]]) -> None:
        if i == len(steps_a) and j == len(steps_b):
            results.append(current[:])
            return
        if i < len(steps_a):
            current.append(("A", steps_a[i]))
            backtrack(i + 1, j, current)
            current.pop()
        if j < len(steps_b):
            current.append(("B", steps_b[j]))
            backtrack(i, j + 1, current)
            current.pop()

    backtrack(0, 0, [])
    return results


def sample_interleavings(
    steps_a: Sequence[Step], steps_b: Sequence[Step], samples: int, seed: int | None = None
) -> List[List[Tuple[str, Step]]]:
    """Return a random sample of valid interleavings.

    This is useful when the full set is too large to enumerate.
    """
    rng = random.Random(seed)
    results: List[List[Tuple[str, Step]]] = []
    for _ in range(samples):
        i = 0
        j = 0
        current: List[Tuple[str, Step]] = []
        while i < len(steps_a) or j < len(steps_b):
            choices = []
            if i < len(steps_a):
                choices.append("A")
            if j < len(steps_b):
                choices.append("B")
            pick = rng.choice(choices)
            if pick == "A":
                current.append(("A", steps_a[i]))
                i += 1
            else:
                current.append(("B", steps_b[j]))
                j += 1
        results.append(current)
    return results


def possible_final_counts(
    steps_a: Sequence[Step], steps_b: Sequence[Step], initial: int = 0
) -> Set[int]:
    """Simulate unsynchronized increments and return possible final values.

    Steps must be from {"read", "inc", "write"}. Each thread has its own local
    register initialized on read. Writes update the shared counter. Missing
    reads mean local is treated as None and should not be written.
    """
    finals: Set[int] = set()
    interleavings = enumerate_interleavings(steps_a, steps_b)
    for schedule in interleavings:
        shared = initial
        local_a = None
        local_b = None
        for thread, step in schedule:
            if thread == "A":
                local_a, shared = _apply_step(step, local_a, shared)
            else:
                local_b, shared = _apply_step(step, local_b, shared)
        finals.add(shared)
    return finals


def _apply_step(step: Step, local: int | None, shared: int) -> Tuple[int | None, int]:
    """Apply a single step to local/shared state for one thread."""
    if step == "read":
        return shared, shared
    if step == "inc":
        if local is None:
            return None, shared
        return local + 1, shared
    if step == "write":
        if local is None:
            return None, shared
        return local, local
    raise ValueError(f"unknown step: {step}")


if __name__ == "__main__":
    steps = ["read", "inc", "write"]
    finals = possible_final_counts(steps, steps)
    print("possible finals:", sorted(finals))
    # TODO: expand with custom steps or sampling for larger cases
