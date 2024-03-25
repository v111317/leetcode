#https://leetcode.com/problems/rotate-image

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
# DO NOT allocate another 2D matrix and do the rotation.
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        #transpose
        for i in range(n):
            for j in range(i, n):
                #print(i, j)
                #print(" => ", matrix[i][j])
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                #print(" => ", matrix[i][j])
        
        #print(matrix)
        #swap columns
        for i in range(n):
            for j in range(n//2):
                #print(i, j)
                #print(n-1-i, j)
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][n-1-j]
                matrix[i][n-1-j] = temp
        #print(matrix)
        
sol1 = Solution()
mat1 = [[1,2,3],[4,5,6],[7,8,9]]
sol1.rotate(mat1)
#print(mat1)
mat2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
sol1.rotate(mat2)
print(mat2)