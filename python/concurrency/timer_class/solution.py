from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional, Protocol


class Runner(Protocol):
    field: str

    def run(self) -> None:
        ...


@dataclass
class ScheduledTask:
    name: str
    delay_seconds: float


class TimerService:
    """Schedule named tasks to run in the future.

    The service accepts a runner object with a `run()` method and a string
    attribute `field`. Tasks should run in named threads after a delay. Cancel
    by name should be a no-op if the task already started.
    """

    def __init__(self, runner: Runner) -> None:
        self._runner = runner
        self._tasks: Dict[str, ScheduledTask] = {}
        # TODO: initialize synchronization primitives and worker threads

    def schedule(self, name: str, delay_seconds: float) -> None:
        """Schedule a task to run after delay_seconds."""
        # TODO: schedule a named task thread-safe
        raise NotImplementedError

    def cancel(self, name: str) -> None:
        """Cancel a scheduled task by name if it has not started."""
        # TODO: safely cancel a pending task
        raise NotImplementedError

    def shutdown(self, timeout: Optional[float] = None) -> None:
        """Stop all scheduling and wait for running tasks to finish."""
        # TODO: implement clean shutdown
        raise NotImplementedError

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
    # TODO: schedule tasks and shutdown
