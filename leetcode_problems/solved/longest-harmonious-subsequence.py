#https://leetcode.com/problems/longest-harmonious-subsequence/description/

# We define a harmonious array as an array where the difference between its maximum value and its minimum value
# is exactly 1.

# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible 
# subsequences.

# A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without 
# changing the order of the remaining elements.
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        numMap = {}
        for num in nums:
            if num in numMap:
                numMap[num] += 1
            else:
                numMap[num] = 1
        
        maxLen = float('-inf')
        keys = list(numMap.keys())
        for key in keys:
            lenSeq = numMap[key]
            if key+1 in numMap:
                lenSeq += numMap[key+1]
            else: 
                lenSeq = 0
            maxLen = max(maxLen, lenSeq)
        
        return maxLen
    
sol1 = Solution()
print(sol1.findLHS([1,3,2,2,5,2,3,7]))
print(sol1.findLHS([1,2,3,4]))
print(sol1.findLHS([1,1,1,1]))

