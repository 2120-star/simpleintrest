from simppleint import simple_interest


def test_simple_interest():
    assert simple_interest(1000, 5, 2) == 100


def test_zero_principal():
    assert simple_interest(0, 5, 2) == 0


def test_zero_time():
    assert simple_interest(1000, 5, 0) == 0