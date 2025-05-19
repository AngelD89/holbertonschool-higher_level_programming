#!/usr/bin/python3
"""
This module defines a function that prints a text with 2 new lines
after each '.', '?' or ':' character.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The input text string.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    for char in text:
        new_text += char
        if char in ".:?":
            new_text += "\n\n"

    for line in new_text.split("\n"):
        print(line.strip())
