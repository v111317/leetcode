#https://leetcode.com/problems/transpose-matrix/description/

# Given a 2D integer array matrix, return the transpose of matrix.

# The transpose of a matrix is the matrix flipped over its main diagonal, 
# switching the matrix's row and column indices.
from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        nRows = len(matrix)
        nCols = len(matrix[0])
        
        if nRows==1 and nCols==1:
            return matrix
        
        transposeMat = [[0 for i in range(nRows)] for i in range(nCols)]
        
        for i in range(0, nRows):
            for j in range(0, nCols):
                
                transposeMat[j][i] = matrix[i][j]
        
        return transposeMat

sol1 = Solution()
print(sol1.transpose([[1,2,3],[4,5,6],[7,8,9]]))
print(sol1.transpose([[1,2,3],[4,5,6]]))
print(sol1.transpose([[1,2,3]]))

#time - O(n*n)
#space - O(n*n)