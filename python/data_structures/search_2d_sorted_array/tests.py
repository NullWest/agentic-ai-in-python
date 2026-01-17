import pytest

from solution import search_2d_sorted


def test_found_middle():
    matrix = [
        [1, 4, 7],
        [2, 5, 9],
        [3, 6, 10],
    ]
    assert search_2d_sorted(matrix, 5) == (1, 1)


def test_not_found():
    matrix = [[1, 2], [3, 4]]
    assert search_2d_sorted(matrix, 8) is None


def test_singleton():
    assert search_2d_sorted([[7]], 7) == (0, 0)


def test_empty_matrix():
    assert search_2d_sorted([], 1) is None


@pytest.mark.xfail(reason="Stretch: handle ragged matrices defensively")
def test_ragged_matrix():
    matrix = [[1, 2, 3], [4, 5]]
    assert search_2d_sorted(matrix, 5) == (1, 1)


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
