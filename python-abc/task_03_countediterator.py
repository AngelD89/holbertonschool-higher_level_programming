#!/usr/bin/env python3
"""CountedIterator: tracks the number of items iterated."""


class CountedIterator:
    """Iterator that counts how many items have been iterated."""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        item = next(self.iterator)  # May raise StopIteration
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items iterated so far."""
        return self.count

    def __iter__(self):
        """Return self to support iteration in for-loops."""
        return self
