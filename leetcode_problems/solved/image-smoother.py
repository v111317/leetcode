#https://leetcode.com/problems/image-smoother/description/

# An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding 
# down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the 
# blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it 
# in the average (i.e., the average of the four cells in the red smoother).

# Given an m x n integer matrix img representing the grayscale of an image, return 
# the image after applying the smoother on each cell of it.

from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])
        
        result = [[0]*cols for i in range(rows)]
        # print(result)
        # return
        for i in range(rows):
            
            for j in range(cols):
                sumNums = 0
                countNums = 0
                if i-1>=0: 
                    if j-1>=0:
                        sumNums += img[i-1][j-1]
                        countNums += 1

                    if j+1<cols:
                        sumNums += img[i-1][j+1]
                        countNums += 1
                    
                    sumNums += img[i-1][j]
                    countNums += 1
                # if i==2 and j==0:
                #     print(sumNums)
                
                if j-1>=0:
                    sumNums += img[i][j-1]
                    countNums += 1
                    
                    if i+1<rows:
                        sumNums += img[i+1][j-1]
                        countNums += 1
                # if i==2 and j==0:
                #     print(sumNums)
                
                if j+1<cols:
                    sumNums += img[i][j+1]
                    countNums += 1
                    
                    # print(" => ", i, cols)
                    if i+1<rows:
                        sumNums += img[i+1][j+1]
                        countNums += 1
                        
                # if i==2 and j==0:
                #     print(sumNums)
                
                if i+1<rows:
                    sumNums += img[i+1][j]
                    countNums += 1
                
                # if i==2 and j==0:
                #     print(sumNums)
                sumNums += img[i][j]
                countNums += 1
                #print(i, j, sumNums, countNums)
                avg = sumNums//countNums
                result[i][j] = avg
        
        return result
        
sol1 = Solution()
# print(sol1.imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))  

list2 = [[100,200,100],[200,50,200],[100,200,100]]
#[[137,141,137],[141,138,141],[137,141,137]] expected
#[[137, 141, 137], [141, 138, 141], [137, 141, 137]]
# print(sol1.imageSmoother(list2))
list3 = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
#output [[4,4,5],[5,6,6],[7,8,9],[10,11,12],[13,13,14]]
#expect [[4,4,5],[5,6,6],[8,9,9],[11,12,12],[13,13,14]]
print(sol1.imageSmoother(list3))