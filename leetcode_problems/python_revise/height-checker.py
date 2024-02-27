#https://leetcode.com/explore/learn/card/sorting/694/comparison-based-sorts/4484/

# A school is trying to take an annual photo of all the students. 
# The students are asked to stand in a single file line in non-decreasing order by height. 
# Let this ordering be represented by the integer array expected 
# where expected[i] is the expected height of the ith student in line.

# You are given an integer array heights representing the current order that the students are standing in. 
# Each heights[i] is the height of the ith student in line (0-indexed).

# Return the number of indices where heights[i] != expected[i].
from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expectedHt = heights.copy()
        for i in range(len(expectedHt)-1):
            for j in range(len(expectedHt)-1-i):
                if expectedHt[j] > expectedHt[j+1]:
                    temp = expectedHt[j]
                    expectedHt[j] = expectedHt[j+1]
                    expectedHt[j+1] = temp
        
        count = 0
        for idx, n in enumerate(heights):
            if n != expectedHt[idx]:
                count += 1
        
        return count

sol1 = Solution()
print(sol1.heightChecker([1,1,4,2,1,3]))
print(sol1.heightChecker([5,1,2,3,4]))
