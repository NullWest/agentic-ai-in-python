import pytest

from solution import search_first_occurrence


def test_basic_first_occurrence():
    assert search_first_occurrence([1, 2, 2, 2, 3], 2) == 1


def test_missing_value():
    assert search_first_occurrence([1, 3, 5], 4) == -1


def test_singleton_match():
    assert search_first_occurrence([9], 9) == 0


def test_empty_array():
    assert search_first_occurrence([], 7) == -1


@pytest.mark.xfail(reason="Stretch: handle very large arrays efficiently")
def test_large_array_first_occurrence():
    arr = [0] * 10_000 + [1] * 10_000
    assert search_first_occurrence(arr, 1) == 10_000


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
