
import pytest

from calculator import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(5, 3) == 15


def test_divide():
    assert divide(20, 4) == 5


def test_negative_numbers():
    assert add(-5, 3) == -2


def test_zero():
    assert multiply(10, 0) == 0


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
