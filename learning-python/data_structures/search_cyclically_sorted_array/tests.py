import pytest

from solution import search_cyclically_sorted


def test_basic_rotation():
    assert search_cyclically_sorted([4, 5, 6, 1, 2, 3], 2) == 4


def test_unrotated():
    assert search_cyclically_sorted([1, 2, 3, 4], 3) == 2


def test_missing_value():
    assert search_cyclically_sorted([30, 40, 50, 5, 10, 20], 35) == -1


def test_singleton():
    assert search_cyclically_sorted([9], 9) == 0


@pytest.mark.xfail(reason="Stretch: handle rotation at last index")
def test_rotation_at_last_index():
    assert search_cyclically_sorted([2, 3, 4, 5, 1], 1) == 4


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
