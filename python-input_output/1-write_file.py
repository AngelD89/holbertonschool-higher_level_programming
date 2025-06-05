#!/usr/bin/python3
"""
Write a string to a text file (UTF8) and return the number of characters written.
"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file.
        text (str): The content to write.

    Returns:
        int: Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
