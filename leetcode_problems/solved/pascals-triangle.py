#https://leetcode.com/problems/pascals-triangle/description/

# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        if numRows==1:
            return result
        
        for i in range(2, numRows+1):
            row = []
            row.append(1)
            if i>=3:
                prevRow = result[i-2]
                for j in range(len(result[i-2])-1):
                    row.append(prevRow[j]+prevRow[j+1])
            row.append(1)
            result.append(row)
        
        return result

sol1 = Solution()
print(sol1.generate(5))
print(sol1.generate(2))
