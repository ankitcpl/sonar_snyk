import pytest
from main import calc

def test_add():
    assert calc.add(2, 3) == 5

def test_divide():
    assert calc.divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calc.divide(1, 0)
