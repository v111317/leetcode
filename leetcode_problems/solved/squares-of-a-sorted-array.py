#https://leetcode.com/problems/squares-of-a-sorted-array/description/

# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i]*nums[i]
        
        nums.sort()
        return nums
    
sol1 = Solution()
print(sol1.sortedSquares([-4,-1,0,3,10]))

#time - O(n)
#space - O(1)