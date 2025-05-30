#!/usr/bin/env python3
"""Defines mixins for swimming and flying, and a Dragon class that uses them."""


class SwimMixin:
    """Provides swimming capability."""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Provides flying capability."""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A mythical creature that can both swim and fly."""
    def roar(self):
        print("The dragon roars!")
