#!/usr/bin/python3
"""
This module contains a function that generates Pascal's Triangle.
"""


def pascal_triangle(n):

    """
    Returns a list of lists of integers representing Pascal’s triangle of n.

    Args:
        n (int): The number of rows of Pascal triangle to generate.

    Returns:
        List[List[int]]:list of lists where sublist represents row of Pascal.
        Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row of the triangle

    for i in range(1, n):
        row = [1]  # Every row starts with a 1
        for j in range(1, i):
            # Calculate the value of the current element
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Every row ends with a 1
        triangle.append(row)

    return triangle
