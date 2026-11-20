#!/usr/bin/python3
"""Module 0-add_integer.

This module provides a function that adds two integers.
Floats are cast to integers before adding.
"""


def add_integer(a, b=98):
    """Add a and b after casting floats to integers.
    Raises TypeError if a or b is not an integer or float.
    """
    inf = float("inf")
    if type(a) not in (int, float) or a != a or abs(a) == inf:
        raise TypeError("a must be an integer")
    if type(b) not in (int, float) or b != b or abs(b) == inf:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
