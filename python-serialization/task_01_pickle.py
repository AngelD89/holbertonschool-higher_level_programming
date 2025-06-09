#!/usr/bin/python3
"""Defines a CustomObject class with pickle-based serialization.
"""
import pickle


class CustomObject:
    """Represents a custom object with name, age, and student status."""

    def __init__(self, name, age, is_student):
        """Initialize the CustomObject."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the attributes of the object."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the object to a file using pickle."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file using pickle."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
