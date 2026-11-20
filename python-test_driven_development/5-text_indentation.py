#!/usr/bin/python3
"""Module 5-text_indentation.

This module provides a function that prints text with two new lines
after each of the characters ., ? and :
"""


def text_indentation(text):
    """Print text with 2 new lines after each ., ? and :
    Spaces at the start and end of each printed line are removed.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text) and text[i] == " ":
        i += 1
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n", end="")
            print()
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
