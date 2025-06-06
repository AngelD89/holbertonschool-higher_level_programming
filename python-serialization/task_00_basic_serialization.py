#!/usr/bin/python3
"""Basic serialization module using JSON for dictionaries.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The file path where the JSON will be saved.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize a dictionary from a JSON file.

    Args:
        filename (str): The file path of the JSON file.

    Returns:
        dict: The deserialized dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
