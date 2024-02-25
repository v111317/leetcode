#https://leetcode.com/problems/island-perimeter/description/

# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, 
# and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. 
# One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. 
# Determine the perimeter of the island.

from typing import List

#revise
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        perimeter = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 1:
                    perimeter += 4

                    if i-1>=0 and grid[i-1][j]==1:
                        perimeter -= 1
                    if j+1<len(grid[i]) and grid[i][j+1]==1:
                        perimeter -= 1
                    if i+1<len(grid) and grid[i+1][j]==1:
                        perimeter -= 1
                    if j-1>=0 and grid[i][j-1]==1:
                        perimeter -= 1
        
        return perimeter
    
    def islandPerimeter2(self, grid: List[List[int]]) -> int:
        
        perimeter = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 1:
                    perimeter += 4
                    #instead of checking all 4 neighbors, check only top and right and deduct 2 for both of them
                    if i-1>=0 and grid[i-1][j]==1:
                        perimeter -= 2
                    if j+1<len(grid[i]) and grid[i][j+1]==1:
                        perimeter -= 2
        
        return perimeter
        
sol1 = Solution()
print(sol1.islandPerimeter2([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
                        
#time - O(n*n)
#space - O(1)
        

            