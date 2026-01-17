# timer_class

## What you are building
Create a timer facility that can schedule a named task to run in the future. The constructor accepts a runner object with a `run()` method and a string field named `field`. You should start a named thread at (or after) the requested time and allow cancellation by name.

Key behaviors:
- Scheduling starts a thread that will call `run()` after a delay.
- Canceling a task should prevent it from running if it has not started.
- Cancel is a no-op if the task is already running or has completed.
- The service should shut down cleanly without deadlocks.

Optional (if you have time): context manager support or timeout helpers.

## Input / Output + Constraints
- Input: a runner object with `run()` and string attribute `field`
- Output: scheduled threads that call `run()` at or after the requested time
- Constraint: thread safety, clean shutdown, safe cancel behavior

## Examples
- Schedule `"alpha"` in 0.1s, then cancel -> `run()` not invoked
- Schedule `"beta"` in 0s -> run immediately
- Schedule two names -> both run once

## Common pitfalls
- Starting a thread immediately rather than waiting for the delay.
- Allowing a canceled task to run because cancelation is not synchronized.
- Deadlocking during shutdown by waiting on threads while holding locks.

## Getting Started
- Implement `TimerService` in `solution.py`.
- First time: from the repo root, build the image: `docker build -t python-assignments .`
- Run tests (Docker): `docker run --rm -v "$PWD":/work -w /work python-assignments pytest -q tests.py`
- Fallback (Docker): `docker run --rm -v "$PWD":/work -w /work python-assignments python tests.py`
