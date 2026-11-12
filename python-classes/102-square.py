#!/usr/bin/python3
"""Defines a class Square that can be compared by area."""


class Square:
    """Defines a square by its size."""

    def __init__(self, size=0):
        """Initialize a square with a size."""
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size, which must be a non-negative number."""
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Return True if areas are equal."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Return True if areas differ."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Return True if this area is smaller."""
        return self.area() < other.area()

    def __le__(self, other):
        """Return True if this area is smaller or equal."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Return True if this area is bigger."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Return True if this area is bigger or equal."""
        return self.area() >= other.area()
