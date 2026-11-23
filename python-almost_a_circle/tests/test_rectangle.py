#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import io
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle."""

    def test_inherits_base(self):
        """Rectangle is a Base."""
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_ids(self):
        """Explicit and automatic ids."""
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)
        a = Rectangle(1, 1)
        b = Rectangle(1, 1)
        self.assertEqual(b.id, a.id + 1)

    def test_getters(self):
        """Attributes are readable."""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 3, 4))

    def test_type_errors(self):
        """Non-integers are rejected."""
        for args in [("2",), (None,), ([],), (1.5,), (True,)]:
            with self.assertRaises(TypeError):
                Rectangle(10, *args)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 0, "a")

    def test_value_errors(self):
        """Out-of-range values are rejected."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 1, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 1, 0, -1)

    def test_setters(self):
        """Setters validate."""
        r = Rectangle(1, 1)
        r.width = 5
        self.assertEqual(r.width, 5)
        with self.assertRaises(ValueError):
            r.width = -10

    def test_area(self):
        """Area is width * height."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_display(self):
        """Display prints # characters."""
        with patch("sys.stdout", new=io.StringIO()) as out:
            Rectangle(2, 2).display()
        self.assertEqual(out.getvalue(), "##\n##\n")
