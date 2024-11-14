import pytest
from main import calculate_balance

def test_calculate_balance():
    assert calculate_balance(1000, 500) == 1500
    assert calculate_balance(500, 1500) == 2000

