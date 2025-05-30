#!/usr/bin/python3
"""Define a class MyList that inherits from list."""


class MyList(list):
    """A subclass of list with a method to print the list sorted."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
