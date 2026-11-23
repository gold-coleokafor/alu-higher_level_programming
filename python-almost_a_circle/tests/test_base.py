#!/usr/bin/python3
"""Unit tests for the Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for Base."""

    def test_auto_ids_increase(self):
        """Ids increment by one for each new instance."""
        a = Base()
        b = Base()
        self.assertEqual(b.id, a.id + 1)

    def test_given_id(self):
        """A given id is used as is."""
        self.assertEqual(Base(12).id, 12)

    def test_given_id_does_not_increment(self):
        """A given id doesn't change the counter."""
        a = Base()
        Base(99)
        b = Base()
        self.assertEqual(b.id, a.id + 1)
    def test_id_89(self):
        """Base(89) keeps the id passed."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """to_json_string(None) returns an empty list string."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """to_json_string([]) returns an empty list string."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_data(self):
        """to_json_string serializes a list of dictionaries."""
        d = [{"id": 1, "width": 2}]
        self.assertEqual(Base.to_json_string(d), '[{"id": 1, "width": 2}]')

    def test_from_json_string(self):
        """from_json_string handles None, empty and data."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 89}]'),
                         [{"id": 89}])

    def test_save_and_load(self):
        """save_to_file and load_from_file round trip."""
        from models.rectangle import Rectangle
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        loaded = Rectangle.load_from_file()
        self.assertEqual(str(loaded[0]), str(r))
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")
