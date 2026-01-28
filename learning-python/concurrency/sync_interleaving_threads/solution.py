from __future__ import annotations

from typing import List

import threading


def run_ordered_printer(limit: int = 100) -> List[int]:
    """Return ordered output from two coordinated threads.

    One thread should emit odd numbers and the other even numbers. The final
    output must be strictly increasing from 1..limit.
    """
    # TODO: coordinate two threads with a Condition/Event to enforce ordering

    last_number = 1
    numbers = []

    condition = threading.Condition()

    def worker(is_odd:bool):
        nonlocal last_number

        while len(numbers) < limit:
            with condition:
                if last_number % 2 == int(is_odd):
                    numbers.append(last_number)
                    last_number += 1

                    condition.notify()
                else:
                    condition.wait()

    odd_thread = threading.Thread(target=worker, args=(True,))
    even_thread = threading.Thread(target=worker, args=(False,))

    odd_thread.start()
    even_thread.start()

    odd_thread.join()
    even_thread.join()

    return numbers

if __name__ == "__main__":
    print(run_ordered_printer(10))
