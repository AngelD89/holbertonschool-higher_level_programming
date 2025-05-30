#!/usr/bin/python3
"""Module with a function that returns attributes and methods of an object.
"""


def lookup(obj):
    """Return list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: Names of the object's
        attributes and methods.
    """
    return dir(obj)
