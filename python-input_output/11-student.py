#!/usr/bin/python3
"""Defines a class Student with serialization and reload."""


class Student:
    """Defines a student by first name, last name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation, filtered by attrs."""
        if (type(attrs) is list and
                all(type(a) is str for a in attrs)):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes using the given dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
