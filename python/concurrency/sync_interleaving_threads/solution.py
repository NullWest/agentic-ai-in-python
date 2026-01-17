from __future__ import annotations

from typing import List


def run_ordered_printer(limit: int = 100) -> List[int]:
    """Return ordered output from two coordinated threads.

    One thread should emit odd numbers and the other even numbers. The final
    output must be strictly increasing from 1..limit.
    """
    # TODO: coordinate two threads with a Condition/Event to enforce ordering
    raise NotImplementedError


if __name__ == "__main__":
    print(run_ordered_printer(10))
