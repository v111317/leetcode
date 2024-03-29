

#https://leetcode.com/problems/set-matrix-zeroes/description

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowList = set()
        colList = set()
        
        i = 0
        j = 0
        isFound = False
        #print(matrix)
        while i < len(matrix):
            j = 0
            while j < len(matrix[0]):
                print(i, j)
                print(" => ", rowList)
                print(" => ", colList)
                if matrix[i][j]==0:
                    rowList.add(i)
                    colList.add(j)
                    #isFound = True
                j += 1 
            i += 1       

        for i in range(len(matrix)):
            if i in rowList:
                matrix[i] = [0 for j in range(len(matrix[0]))]
                
        for i in range(len(matrix)):
            if i in rowList:
                i += 1
                continue
            for j in range(len(matrix[0])):
                if j in colList:
                    matrix[i][j] = 0
                    continue

mat1 = [[1,1,1],[1,0,1],[1,1,1]]
sol1 = Solution()
mat2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
mat3 = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
#[[0,0,0,0],[0,0,0,4],[0,0,0,0],[0,0,0,3],[0,0,0,0]]

sol1.setZeroes(mat2)
print(mat2)
#[[0,0,0,0],[0,0,0,4],[0,0,0,4],[0,0,0,3],[0,0,0,1]]