#!/usr/bin/env python3
"""Defines an abstract Animal class with concrete subclasses Dog and Cat."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by all subclasses."""
        pass


class Dog(Animal):
    """Dog subclass that implements the sound method."""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat subclass that implements the sound method."""

    def sound(self):
        return "Meow"
