#https://leetcode.com/problems/toeplitz-matrix/description/

# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in range(rows-1, -1, -1):
            row = i
            col = 0
            val = matrix[row][col]
            
            while row < rows and col < cols:
                if matrix[row][col]!=val:
                    return False
                row += 1
                col += 1
        
        for i in range(1, cols):
            row = 0
            col = i
            val = matrix[row][col]
            
            while row < rows and col < cols:
                if matrix[row][col]!=val:
                    return False
                row += 1
                col += 1
            
        return True
    
    def isToeplitzMatrix2(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in range(1, rows):
            for j in range(1, cols):
                if i>=0 and j>=0 and i<rows and j<cols:
                    if matrix[i][j]!=matrix[i-1][j-1]:
                        return False
        return True
    
sol1 = Solution()
print(sol1.isToeplitzMatrix2([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
print(sol1.isToeplitzMatrix2([[1,2],[2,2]]))
        
