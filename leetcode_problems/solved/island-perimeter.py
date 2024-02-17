from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        landMap = {}
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
        
sol1 = Solution()
print(sol1.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
                        
        

            