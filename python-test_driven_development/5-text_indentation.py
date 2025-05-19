#!/usr/bin/python3
"""
Module for text indentation.
This module provides a function to format text with specific indentation rules.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' characters.

    Args:
        text: The text to print (must be a string)

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Characters to look for
    special_chars = ['.', '?', ':']

    # Process each character
    i = 0
    while i < len(text):
        # Print current character
        print(text[i], end="")

        # If current character is special, print two new lines
        if text[i] in special_chars:
            print("\n")
            # Skip spaces after special character
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue

        i += 1
