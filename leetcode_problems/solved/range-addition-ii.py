#https://leetcode.com/problems/range-addition-ii/description/

# You are given an m x n matrix M initialized with all 0's and an array of operations ops, 
# where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

# Count and return the number of maximum integers in the matrix after performing all the operations.
from typing import List

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        minX = m
        minY = n
        
        for numRange in ops:
            if numRange[0]<=m:
                minX = min(minX, numRange[0])
            else:
                minX = min(minX, m)
                
            if numRange[1]<=n:
                minY = min(minY, numRange[1])
            else:
                minY = min(minY, n)
                
        return minX * minY

sol1 = Solution()
print(sol1.maxCount(3, 3, [[2,2],[3,3]]))
ops1 = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
print(sol1.maxCount(3, 3, ops1))
print(sol1.maxCount(3, 3, []))