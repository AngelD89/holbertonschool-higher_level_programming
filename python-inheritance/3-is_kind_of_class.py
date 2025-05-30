#!/usr/bin/python3
"""Defines a function to check object inheritance or instance."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a_class, otherwise False.
    """
    return isinstance(obj, a_class)
