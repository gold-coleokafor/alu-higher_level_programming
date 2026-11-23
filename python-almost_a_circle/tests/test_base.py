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
