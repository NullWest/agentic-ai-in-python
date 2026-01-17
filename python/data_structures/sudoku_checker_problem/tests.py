import pytest

from solution import is_valid_sudoku


VALID_PARTIAL = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


def test_valid_partial_board():
    assert is_valid_sudoku(VALID_PARTIAL) is True


def test_row_duplicate():
    board = [row[:] for row in VALID_PARTIAL]
    board[0][1] = 5
    assert is_valid_sudoku(board) is False


def test_column_duplicate():
    board = [row[:] for row in VALID_PARTIAL]
    board[0][0] = 6
    assert is_valid_sudoku(board) is False


def test_subgrid_duplicate():
    board = [row[:] for row in VALID_PARTIAL]
    board[1][1] = 9
    assert is_valid_sudoku(board) is False


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
