import time
import pytest

from solution import TimerService


class RecordingRunner:
    def __init__(self) -> None:
        self.field = "record"
        self.calls = []

    def run(self) -> None:
        self.calls.append(time.time())


def test_schedule_immediate_runs():
    runner = RecordingRunner()
    service = TimerService(runner)
    service.schedule("now", 0.0)
    time.sleep(0.05)
    service.shutdown(timeout=1.0)
    assert len(runner.calls) == 1


def test_cancel_prevents_run():
    runner = RecordingRunner()
    service = TimerService(runner)
    service.schedule("later", 0.2)
    service.cancel("later")
    time.sleep(0.25)
    service.shutdown(timeout=1.0)
    assert runner.calls == []


def test_multiple_tasks_run_once():
    runner = RecordingRunner()
    service = TimerService(runner)
    service.schedule("a", 0.0)
    service.schedule("b", 0.0)
    time.sleep(0.05)
    service.shutdown(timeout=1.0)
    assert len(runner.calls) == 2


@pytest.mark.xfail(reason="Stretch: support rescheduling same name")
def test_reschedule_name():
    runner = RecordingRunner()
    service = TimerService(runner)
    service.schedule("task", 0.2)
    service.schedule("task", 0.0)
    time.sleep(0.05)
    service.shutdown(timeout=1.0)
    assert len(runner.calls) == 1


@pytest.mark.xfail(reason="Stretch: ensure shutdown waits for running task")
def test_shutdown_waits():
    runner = RecordingRunner()
    service = TimerService(runner)
    service.schedule("slow", 0.0)
    service.shutdown(timeout=1.0)
    assert len(runner.calls) == 1


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
