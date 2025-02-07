#!/usr/bin/python3
def island_perimeter(grid):
    perimeter = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # Check the four possible adjacent cells
                if i == 0 or grid[i-1][j] == 0:  # Top
                    perimeter += 1
                if i == len(grid) - 1 or grid[i+1][j] == 0:  # Bottom
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:  # Left
                    perimeter += 1
                if j == len(grid[0]) - 1 or grid[i][j+1] == 0:  # Right
                    perimeter += 1
                
    return perimeter
