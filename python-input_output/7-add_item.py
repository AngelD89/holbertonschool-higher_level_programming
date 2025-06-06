#!/usr/bin/python3
"""Adds all arguments to a list and saves them to add_item.json.
"""
import sys
import os.path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


filename = "add_item.json"

# Load existing items if file exists
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add new arguments (excluding script name)
items.extend(sys.argv[1:])

# Save the updated list to add_item.json as JsON
save_to_json_file(items, filename)
