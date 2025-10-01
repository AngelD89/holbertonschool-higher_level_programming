#!/usr/bin/env python3
"""Module for CountedIterator that tracks number of items iterated."""


class CountedIterator:
    """Custom iterator wrapper that counts how many items have been iterated."""

    def __init__(self, iterable):
        self.iterator = iter(iterable)  # create an iterator from the iterable
        self.count = 0  # counter for items iterated

    def __iter__(self):
        """Return the iterator itself."""
        return self

    def __next__(self):
        """Fetch next item, increment count, and return item."""
        item = next(self.iterator)  # may raise StopIteration naturally
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items iterated so far."""
        return self.count
