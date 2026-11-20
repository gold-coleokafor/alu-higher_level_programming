#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function."""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 2, 3, 4]), 9)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 7, 3, 4]), 7)

    def test_one_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -2, -9]), -2)

    def test_mixed_signs(self):
        self.assertEqual(max_integer([-5, 0, 3, -1]), 3)

    def test_duplicates(self):
        self.assertEqual(max_integer([4, 4, 4]), 4)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_int_and_float(self):
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_strings(self):
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_string_argument(self):
        self.assertEqual(max_integer("abc"), "c")

    def test_tuple_argument(self):
        self.assertEqual(max_integer((1, 5, 3)), 5)

    def test_mixed_types_raise(self):
        with self.assertRaises(TypeError):
            max_integer([1, "a"])

    def test_none_raises(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_int_raises(self):
        with self.assertRaises(TypeError):
            max_integer(5)


if __name__ == "__main__":
    unittest.main()
