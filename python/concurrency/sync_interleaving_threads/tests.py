import pytest

from solution import run_ordered_printer


def test_default_limit():
    output = run_ordered_printer()
    assert output == list(range(1, 101))


def test_small_limit():
    assert run_ordered_printer(5) == [1, 2, 3, 4, 5]


def test_limit_one():
    assert run_ordered_printer(1) == [1]


def test_even_limit():
    assert run_ordered_printer(2) == [1, 2]


@pytest.mark.xfail(reason="Stretch: ensure stable ordering under heavy contention")
def test_large_limit():
    output = run_ordered_printer(1000)
    assert output == list(range(1, 1001))


@pytest.mark.xfail(reason="Stretch: support limit zero")
def test_zero_limit():
    assert run_ordered_printer(0) == []


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
