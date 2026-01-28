from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Protocol

import threading
import time

class Runner(Protocol):
    field: str

    def run(self) -> None:
        ...


@dataclass
class ScheduledTask:
    name: str
    delay_seconds: float
    stop_event: threading.Event


class TimerService:
    """Schedule named tasks to run in the future.

    The service accepts a runner object with a `run()` method and a string
    attribute `field`. Tasks should run in named threads after a delay. Cancel
    by name should be a no-op if the task already started.
    """

    def __init__(self, runner: Runner) -> None:
        self._runner = runner
        self._tasks: Dict[str, ScheduledTask] = {}
        self._threads: List[threading.Thread] = []
        self._lock = threading.Lock()

    def schedule(self, name: str, delay_seconds: float) -> None:
        """Schedule a task to run after delay_seconds."""

        with self._lock:
            self._tasks[name] = ScheduledTask(name, delay_seconds, threading.Event())

        def worker():
            time.sleep(delay_seconds)

            with self._lock:
                if not self._tasks[name].stop_event.is_set():
                    self._runner.run()

                    self._tasks[name].stop_event.set()

        thread = threading.Thread(target=worker)

        self._threads.append(thread)

        thread.start()


    def cancel(self, name: str) -> None:
        """Cancel a scheduled task by name if it has not started."""

        with self._lock:
            if self._tasks.get(name):
                self._tasks[name].stop_event.set()


    def shutdown(self, timeout: Optional[float] = None) -> None:
        """Stop all scheduling and wait for running tasks to finish."""

        if timeout:
            time.sleep(timeout)

        with self._lock:
            if self._tasks:
                for task in self._tasks.values():
                    task.stop_event.set()

        if self._threads:
            [thread.join() for thread in self._threads]

    def __enter__(self) -> "TimerService":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.shutdown(timeout=2.0)


if __name__ == "__main__":
    class DemoRunner:
        field = "demo"

        def run(self) -> None:
            print("running", self.field)

    service = TimerService(DemoRunner())