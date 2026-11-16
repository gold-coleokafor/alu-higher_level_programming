#!/usr/bin/python3
"""Defines a class that only allows the attribute first_name."""


class LockedClass:
    """Prevents creating instance attributes other than first_name."""
    __slots__ = ["first_name"]
