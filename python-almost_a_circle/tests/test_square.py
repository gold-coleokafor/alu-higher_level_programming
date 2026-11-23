#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for Square."""

    def test_inherits(self):
        """Square is a Rectangle."""
        self.assertIsInstance(Square(1), Rectangle)

    def test_str(self):
        """__str__ format."""
        self.assertEqual(str(Square(5, 0, 0, 1)), "[Square] (1) 0/0 - 5")

    def test_area(self):
        """Area of a square."""
        self.assertEqual(Square(5).area(), 25)

    def test_validation(self):
        """Validation is inherited."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -1)
