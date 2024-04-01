#https://leetcode.com/problems/search-a-2d-matrix/description/

# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        start = 0
        end = rows - 1
        
        while start <= end:
            mid = (start+end)//2
            
            if matrix[mid][cols-1]==target or matrix[mid][0]==target:
                return True
            
            if target < matrix[mid][0]:
                end = mid - 1
            elif target > matrix[mid][cols-1]:
                start = mid + 1
            else:
                rowMatched = mid
                newStart = 0
                newEnd = cols - 1
                
                while newStart <= newEnd:
                    newMid = (newStart+newEnd)//2
                    
                    if target == matrix[rowMatched][newMid]:
                        return True
                    
                    if target > matrix[rowMatched][newMid]:
                        newStart = newMid + 1
                    else:
                        newEnd = newMid - 1
                break
        return False
sol1 = Solution()
# print(sol1.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(sol1.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))