#!/usr/bin/python3
"""Defines the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square using Rectangle's logic."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set width and height to value, with width validation."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assign attributes by position (id, size, x, y) or by keyword."""
        if args:
            for name, value in zip(("id", "size", "x", "y"), args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                setattr(self, name, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
