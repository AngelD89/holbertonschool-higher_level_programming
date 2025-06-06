#!/usr/bin/python3
"""Module that creates an object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """Creates a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The deserialized Python object.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
