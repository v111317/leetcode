#https://leetcode.com/problems/flipping-an-image/description/

# Given an n x n binary matrix image, flip the image horizontally, then invert it, 
# and return the resulting image.
# To flip an image horizontally means that each row of the image is reversed.
# For example, flipping [1,1,0] horizontally results in [0,1,1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
# For example, inverting [0,1,1] results in [1,0,0].
from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        
        #flip
        for i in range(n):
            for j in range(int(n/2)):
                temp = image[i][j]
                image[i][j] = image[i][n-j-1]
                image[i][n-j-1] = temp
        
        #invert
        for i in range(n):
            for j in range(n):
                image[i][j] = int(not bool(image[i][j]))
                
        return image
    
sol1 = Solution()
print(sol1.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
print(sol1.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))

#time - 
#space - 