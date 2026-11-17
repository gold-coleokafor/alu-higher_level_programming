#!/usr/bin/python3
"""Defines a class BaseGeometry with an unimplemented area."""


class BaseGeometry:
    """Base class for geometry."""

    def area(self):
        """Raise an Exception, since area is not implemented."""
        raise Exception("area() is not implemented")
