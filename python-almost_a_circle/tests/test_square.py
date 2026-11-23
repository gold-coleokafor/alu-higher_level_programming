#!/usr/bin/python3
"""Unit tests for the Square class."""
import os
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

    def test_square_1_2_3(self):
        """Square(1, 2, 3) sets size, x and y."""
        s = Square(1, 2, 3)
        self.assertEqual((s.size, s.x, s.y), (1, 2, 3))

    def test_square_1_str_2(self):
        """Square(1, "2") raises TypeError for x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")

    def test_square_1_2_str_3(self):
        """Square(1, 2, "3") raises TypeError for y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_square_minus_1(self):
        """Square(-1) raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_square_1_2_minus_3(self):
        """Square(1, 2, -3) raises ValueError for y."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)

    def test_to_dictionary_square(self):
        """to_dictionary() returns id, size, x and y."""
        s = Square(1, 2, 3, 89)
        self.assertEqual(s.to_dictionary(),
                         {"id": 89, "size": 1, "x": 2, "y": 3})

    def test_update_no_args(self):
        """update() changes nothing."""
        s = Square(1, 2, 3, 89)
        s.update()
        self.assertEqual(s.to_dictionary(),
                         {"id": 89, "size": 1, "x": 2, "y": 3})

    def test_update_args(self):
        """update(89), (89, 1), (89, 1, 2), (89, 1, 2, 3)."""
        s = Square(5)
        s.update(89)
        self.assertEqual(s.id, 89)
        s.update(89, 1)
        self.assertEqual(s.size, 1)
        s.update(89, 1, 2)
        self.assertEqual(s.x, 2)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_update_kwargs(self):
        """update(**{ 'id': 89 }) and longer dictionaries."""
        s = Square(5)
        s.update(**{ 'id': 89 })
        self.assertEqual(s.id, 89)
        s.update(**{ 'id': 89, 'size': 1 })
        self.assertEqual(s.size, 1)
        s.update(**{ 'id': 89, 'size': 1, 'x': 2 })
        self.assertEqual(s.x, 2)
        s.update(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })
        self.assertEqual(s.y, 3)

    def test_create(self):
        """Square.create with growing dictionaries."""
        s = Square.create(**{ 'id': 89 })
        self.assertEqual(s.id, 89)
        s = Square.create(**{ 'id': 89, 'size': 1 })
        self.assertEqual(s.size, 1)
        s = Square.create(**{ 'id': 89, 'size': 1, 'x': 2 })
        self.assertEqual(s.x, 2)
        s = Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })
        self.assertEqual(s.to_dictionary(),
                         {"id": 89, "size": 1, "x": 2, "y": 3})

    def test_save_to_file_none(self):
        """Square.save_to_file(None) writes an empty list."""
        Square.save_to_file(None)
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """Square.save_to_file([]) writes an empty list."""
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_one(self):
        """Square.save_to_file([Square(1)]) writes one dictionary."""
        Square.save_to_file([Square(1, 0, 0, 7)])
        with open("Square.json") as f:
            self.assertEqual(
                Square.from_json_string(f.read()),
                [{"id": 7, "size": 1, "x": 0, "y": 0}])

    def test_load_from_file_missing(self):
        """Square.load_from_file() when the file doesn't exist."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_exists(self):
        """Square.load_from_file() when the file exists."""
        Square.save_to_file([Square(3, 1, 2, 9)])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(str(loaded[0]), "[Square] (9) 1/2 - 3")

    def tearDown(self):
        """Remove the JSON file created by a test."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
