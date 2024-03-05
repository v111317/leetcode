#https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/

# Given an integer array nums that does not contain any zeros, 
# find the largest positive integer k such that -k also exists in the array.

# Return the positive integer k. If there is no such integer, return -1.
from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        maxNum = -1
        numMap = {}
        for num in nums:
            if num < 0:
                key = -num
                value = -1
            else:
                key = num
                value = 1
            
            if key not in numMap:
                numMap[key] = value
            else:
                valuePresent = numMap[key]
                if valuePresent + value==0:
                    maxNum = max(maxNum, key)
        return maxNum
    
sol1 = Solution()
print(sol1.findMaxK([-1,2,-3,3]))
print(sol1.findMaxK([-1,10,6,7,-7,1]))
print(sol1.findMaxK([-10,8,6,7,-2,-3]))

#time - O(n)
#space - O(n)
                 
