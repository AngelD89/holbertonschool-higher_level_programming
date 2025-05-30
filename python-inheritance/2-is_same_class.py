#!/usr/bin/python3
"""Defines a function to check exact instance of a class."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class; else False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
