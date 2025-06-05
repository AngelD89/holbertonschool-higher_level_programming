#!/usr/bin/python3
"""Module for writing a string to a UTF-8 text file.
"""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 text file and returns the number of characters written.

    Overwrites the file if it exists, creates it if it doesn't.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
