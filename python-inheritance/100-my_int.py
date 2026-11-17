#!/usr/bin/python3
"""Defines a class MyInt that inverts == and !=."""


class MyInt(int):
    """A rebel integer with inverted equality operators."""

    def __eq__(self, other):
        """Return True when the values differ."""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Return True when the values are equal."""
        return int.__eq__(self, other)
