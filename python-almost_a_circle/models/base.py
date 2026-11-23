#!/usr/bin/python3
"""Defines the Base class."""


class Base:
    """Manages the id attribute for all other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize with a given id or an auto-incremented one."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
