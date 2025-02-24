"""
This module provides basic mathmatical test functions.
"""

from src.string_utils import reverse_string, is_palindrome, count_vowels


def test_reverse_string():
    """
    Tests the ability of the reverse string function

    Tests:
        Normal word
        Palindrone
    """

    assert reverse_string("testing") == "gnitset"
    assert reverse_string("racecar") == "racecar"


def test_is_palindrome():
    """
    Tests the ability of the palindrome function

    Tests:
        Normal word
        Palindrone
    """

    assert is_palindrome("testing") is False
    assert is_palindrome("racecar") is True


def test_count_vowels():
    """
    Tests the ability of the count vowels function

    Tests:
        Words containing a, e, i, o, u
    """

    assert count_vowels("testing") == 2
    assert count_vowels("racecar") == 3
    assert count_vowels("count") == 2
