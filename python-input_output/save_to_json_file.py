#!/usr/bin/python3
"""Writes a Python object to a text file using JSON format."""
import json

def save_to_json_file(my_obj, filename):
    """Saves an object to a file in JSON format."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
