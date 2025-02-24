"""
This module provides basic mathmatical test functions.
"""

import pytest
from src.math_utils import add, subtract, multiply, divide


def test_add():
    """
    Tests the ability of the add function

    Tests:
        Positive with positive
        Positive with negative
        Negative with negative
    """

    assert add(3, 2) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2


def test_subtract():
    """
    Tests the ability of the subtract function

    Tests:
        Positive with positive
        Positive with negative
        Negative with negative
        Negative outcome
    """

    assert subtract(3, 2) == 1
    assert subtract(3, 3) == 0
    assert subtract(2, 3) == -1
    assert subtract(-1, -1) == 0
    assert subtract(-1, 2) == -3


def test_multiply():
    """
    Tests the ability of the multiply function

    Tests:
        Positive with positive
        Positive with negative
        Negative with negative
    """

    assert multiply(3, 2) == 6
    assert multiply(-1, 1) == -1
    assert multiply(-1, -2) == 2
    assert multiply(0, 2) == 0


def test_divide():
    """
    Tests the ability of the divide function

    Tests:
        Positive with positive
        Positive with negative
        Negative with negative
        Divide by zero
    """

    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5
    assert divide(10, -5) == -2
    assert divide(-10, -5) == 2

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
