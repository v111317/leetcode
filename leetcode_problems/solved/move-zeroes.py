#https://leetcode.com/problems/move-zeroes/description/

# Given an integer array nums, move all 0's to the end of it while maintaining 
# the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        
        zeroTracker = 0
        numTracker = 0
        while numTracker < len(nums):
            
            if nums[zeroTracker]==0 and nums[numTracker]!=0:
                temp = nums[numTracker]
                nums[numTracker] = nums[zeroTracker]
                nums[zeroTracker] = temp
                
            if nums[zeroTracker]!=0:
                zeroTracker += 1
            numTracker += 1
        return nums

sol1 = Solution()
# print(sol1.moveZeroes([0,1,0,3,12]))  
print(sol1.moveZeroes([1,0]))                
#time - O(n)
#space - O(1)
                
            