#!/usr/bin/python3
"""Defines a function that writes to a text file."""


def write_file(filename="", text=""):
    """Write text to a UTF8 file (overwriting) and return the count."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
