#!/usr/bin/env python3
"""Module for VerboseList extending Python's built-in list with notifications."""


class VerboseList(list):
    """Custom list that prints notifications on modifications."""

    def append(self, item):
        """Append item and notify."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend list and notify with number of items added."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove item and notify."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop item and notify."""
        item = self[index]  # peek before popping
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
