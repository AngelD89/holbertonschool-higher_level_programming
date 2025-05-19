#!/usr/bin/python3
"""
Module for dividing matrix elements.
This module provides a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix: A list of lists of integers or floats
        div: Number to divide by (int or float)

    Returns:
        A new matrix with all elements divided by div,
        rounded to 2 decimal places

    Raises:
        TypeError: If matrix is not a list of lists of numbers,
                   if rows have different sizes, or if div is not a number
        ZeroDivisionError: If div is 0
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err_msg)

    # Check if matrix contains only lists
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(err_msg)
        # Check if all elements are integers or floats
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(err_msg)

    # Check if all rows have the same size
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create a new matrix with divided values
    new_matrix = []
    for row in matrix:
        new_row = [round(item / div, 2) for item in row]
        new_matrix.append(new_row)

    return new_matrix
