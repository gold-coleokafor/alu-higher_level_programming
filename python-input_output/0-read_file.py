#!/usr/bin/python3
"""Defines a function that reads a text file."""


def read_file(filename=""):
    """Read a UTF8 text file and print it to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
