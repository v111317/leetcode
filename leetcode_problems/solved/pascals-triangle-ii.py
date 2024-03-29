#https://leetcode.com/problems/pascals-triangle-ii/description/

# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [[1]]
        if rowIndex==0:
            return result
        
        for i in range(1, rowIndex+1):
            row = []
            row.append(1)
            if i>=2:
                prevRow = result[i-1]
                for j in range(len(result[i-1])-1):
                    row.append(prevRow[j]+prevRow[j+1])
            row.append(1)
            result.append(row)
        
        return result[rowIndex]
    
sol1 = Solution()
print(sol1.getRow(1))
print(sol1.getRow(2))
print(sol1.getRow(3))
print(sol1.getRow(4))
print(sol1.getRow(5))
