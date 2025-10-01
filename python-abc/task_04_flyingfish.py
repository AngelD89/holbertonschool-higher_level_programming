#!/usr/bin/env python3
"""Module demonstrating multiple inheritance with a FlyingFish class."""


class Fish:
    """Represents a Fish."""

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """Represents a Bird."""

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a Flying Fish, inheriting from Fish and Bird."""

    def swim(self):
        print("The flying fish is swimming!")

    def fly(self):
        print("The flying fish is soaring!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
