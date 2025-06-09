#!/usr/bin/python3
"""Convert CSV data to JSON format and write to a file."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to a JSON file named 'data.json'.

    Args:
        csv_filename (str): The name of the input CSV file.

    Returns:
        bool: True if conversion is successful, False otherwise.
    """
    try:
        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except Exception:
        return False
