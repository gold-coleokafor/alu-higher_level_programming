#!/usr/bin/python3
"""Defines a function that describes an object as a dictionary."""


def class_to_json(obj):
    """Return the dictionary description of obj for JSON serialization."""
    return obj.__dict__
