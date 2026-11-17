#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """A list with a method to print itself sorted."""

    def print_sorted(self):
        """Print the list in ascending order without changing it."""
        print(sorted(self))
