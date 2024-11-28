#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): The 2D matrix to rotate.
    """
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            # Save the top element
            top = matrix[first][i]
            # Move left element to top
            matrix[first][i] = matrix[n - 1 - i][first]
            # Move bottom element to left
            matrix[n - 1 - i][first] = matrix[last][n - 1 - i]
            # Move right element to bottom
            matrix[last][n - 1 - i] = matrix[i][last]
            # Assign top element to right
            matrix[i][last] = top
