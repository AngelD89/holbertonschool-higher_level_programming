#!/usr/bin/python3
"""
Module for adding integers.
This module provides a simple function for adding two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers and returns the result.

    Args:
        a: first number to add
        b: second number to add, defaults to 98

    Returns:
        The addition of a and b as an integer

    Raises:
        TypeError: If a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
