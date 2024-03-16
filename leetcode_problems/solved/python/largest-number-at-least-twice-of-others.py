#https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/

# You are given an integer array nums where the largest integer is unique.

# Determine whether the largest element in the array is at least twice as much as every other number in the array. 
# If it is, return the index of the largest element, or return -1 otherwise.
from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxNum = -1
        maxIdx = -1
        for i, num in enumerate(nums):
            if num > maxNum:
                maxNum = num
                maxIdx = i
            
        for num in nums:
            if num==maxNum:
                continue
            if num*2>maxNum:
                return -1
        return maxIdx

sol1 = Solution()
print(sol1.dominantIndex([3,6,1,0]))