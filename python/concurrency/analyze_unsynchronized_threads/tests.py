import pytest

from solution import enumerate_interleavings, possible_final_counts


def test_interleavings_count_small():
    steps_a = ["read", "write"]
    steps_b = ["read"]
    interleavings = enumerate_interleavings(steps_a, steps_b)
    assert len(interleavings) == 3


def test_possible_final_counts_racy_increment():
    steps = ["read", "inc", "write"]
    assert possible_final_counts(steps, steps) == {1, 2}


def test_possible_final_counts_empty():
    assert possible_final_counts([], []) == {0}


def test_possible_final_counts_read_write_only():
    assert possible_final_counts(["read", "write"], ["read", "write"]) == {0}


@pytest.mark.xfail(reason="Stretch: handle large interleavings efficiently")
def test_large_interleavings_count():
    steps_a = ["read", "inc", "write"] * 4
    steps_b = ["read", "inc", "write"] * 4
    interleavings = enumerate_interleavings(steps_a, steps_b)
    assert len(interleavings) > 0


@pytest.mark.xfail(reason="Stretch: validate unknown steps earlier")
def test_unknown_step():
    with pytest.raises(ValueError):
        possible_final_counts(["read", "boom"], [])


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
