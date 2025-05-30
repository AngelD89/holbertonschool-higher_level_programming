#!/usr/bin/python3
"""Module containing a function that returns attributes and methods of an object.
"""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings containing the names of the object's
        attributes and methods.
    """
    return dir(obj)
