#https://leetcode.com/problems/longest-consecutive-sequence/description/

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.
from typing import List

class Solution:
    #time limit exceeded
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        
        numMap = {}
        for n in nums:
            if n not in numMap:
                numMap[n] = 1
        
        
        for idx, n in enumerate(nums):
            
            num = n
            count = 0
            if num-1 not in numMap:
                while num in numMap:
                    num += 1
                    count += 1
                if count > maxLen:
                    maxLen = count
        
        return maxLen
    
sol1 = Solution()
print(sol1.longestConsecutive([100,4,200,1,3,2]))
print(sol1.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))