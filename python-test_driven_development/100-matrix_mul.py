#!/usr/bin/python3
"""Module 100-matrix_mul.

This module provides a function that multiplies two matrices.
"""


def matrix_mul(m_a, m_b):
    """Return the product of the matrices m_a and m_b."""
    pairs = (("m_a", m_a), ("m_b", m_b))
    for name, m in pairs:
        if not isinstance(m, list):
            raise TypeError("{} must be a list".format(name))
    for name, m in pairs:
        for row in m:
            if not isinstance(row, list):
                raise TypeError("{} must be a list of lists".format(name))
    for name, m in pairs:
        if len(m) == 0 or len(m[0]) == 0:
            raise ValueError("{} can't be empty".format(name))
    for name, m in pairs:
        for row in m:
            for n in row:
                if type(n) not in (int, float):
                    raise TypeError(
                        "{} should contain only integers or floats"
                        .format(name))
    for name, m in pairs:
        for row in m:
            if len(row) != len(m[0]):
                raise TypeError(
                    "each row of {} must be of the same size".format(name))
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = []
    for row in m_a:
        new_row = []
        for j in range(len(m_b[0])):
            total = 0
            for k in range(len(m_b)):
                total += row[k] * m_b[k][j]
            new_row.append(total)
        result.append(new_row)
    return result
