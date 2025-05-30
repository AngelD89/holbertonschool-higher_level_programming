#!/usr/bin/python3
"""Defines a function that checks for inherited instances."""
  

def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a subclass (not the class itself),
        otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
