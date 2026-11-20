#!/usr/bin/python3
"""Module 101-lazy_matrix_mul.

This module multiplies two matrices using NumPy.
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Return the product of m_a and m_b using numpy.matmul."""
    return numpy.matmul(m_a, m_b)
