"""
This module provides basic string utility functions.
"""


def reverse_string(string):
    """
    Return the reverse of the given word.

    Args:
        string (string): Word to reverse.

    Returns:
        boolean: The reverse of the provided word.
    """

    return string[::-1]


def is_palindrome(string):
    """
    Returns whether the string is a palindrome.

    Args:
        string (string): Word to calculate if its a palindrome.

    Returns:
        boolean: The reverse of the provided word.
    """
    word = string.lower()
    return word == word[::-1]


def count_vowels(string):
    """
    Returns the amount of vowels in the word.

    Args:
        number (int): Number of vowels in the word.

    Returns:
        int: The number of vowels in the word.
    """

    vowels = "aeiou"
    count = 0

    for char in string.lower():
        if char in vowels:
            count += 1

    return count
