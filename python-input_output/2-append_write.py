#!/usr/bin/python3
"""Module for appending a string to a text file (UTF8).
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
