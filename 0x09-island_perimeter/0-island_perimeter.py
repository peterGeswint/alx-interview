#!/usr/bin/python3
"""
Island Perimeter Calculation Module

This module provides a function to calculate the perimeter of an island
described in a grid. The grid is a 2D list of integers where 0 represents
water and 1 represents land.

Example usage:
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))  # Output: 12

Attributes:
    None

Functions:
    island_perimeter(grid)
        Calculates the perimeter of the island in the given grid.

"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.
    Args:
    grid(List[List[int]]):2D grd representaton of iland, wher0reprsentwaterand1
    rprsntland.

    Returns:
    int: The perimeter of the island.
    The function iterates over each cell in the grid.Foreachlandcell(value1),
    it checks its four adjacent cells(top,bottom,left,right).Ifanadjacentcell
    is water (value0)oroutofthegrid'sbounds,itcontributestotheperimeter.
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # Check the top adjacent cell
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check the bottom adjacent cell
                if i == len(grid) - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Check the left adjacent cell
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check the right adjacent cell
                if j == len(grid[0]) - 1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter
