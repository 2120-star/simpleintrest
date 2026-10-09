
from simppleint import simple_interest

def test_simple_interest():
    assert simple_interest(10000, 5, 2) == 1000

def test_zero_interest():
    assert simple_interest(5000, 0, 2) == 0

def test_one_year():
    assert simple_interest(2000, 10, 1) == 200
