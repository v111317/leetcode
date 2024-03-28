#https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/

# Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence 
# (i.e. subarray). The subsequence must be strictly increasing.

# A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is 
# [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].
from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        
        maxLen = 1
        n = len(nums)
        count = 1
        for i in range(n-1):
            if nums[i+1] > nums[i]:
                count += 1
            else:
                count = 1
            maxLen = max(maxLen, count)
            
        return maxLen

sol1 = Solution()
print(sol1.findLengthOfLCIS([1,3,5,4,7]))
print(sol1.findLengthOfLCIS([2,2,2,2,2]))

#time - O(n)
#space - O(1)