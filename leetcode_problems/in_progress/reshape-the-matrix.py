#https://leetcode.com/problems/reshape-the-matrix/description/

# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one 
# with a different size r x c keeping its original data.

# You are given an m x n matrix mat and two integers r and c representing the number of rows and 
# the number of columns of the wanted reshaped matrix.

# The reshaped matrix should be filled with all the elements of the original matrix in the same 
# row-traversing order as they were.

# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; 
# Otherwise, output the original matrix.
from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        
        if rows*cols!=r*c:
            return mat
        
        result = [[0]*c]
        i = 0
        j = 0
        for row in mat:
            for cell in row:
                a = 1    