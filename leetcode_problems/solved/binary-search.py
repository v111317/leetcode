#https://leetcode.com/problems/binary-search/description/

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.
from typing import List

#revise
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            if target in nums:
                return 0
            else:
                return -1
        
        start = 0
        end = len(nums)-1
        mid = end // 2
        
        while start <= end:
            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                return mid
            mid = (end+start)//2
        return -1
    
sol1 = Solution()
print(sol1.search([-1,0,3,5,9,12], 8))
print(sol1.search([2,5], 5))

#time - O(logn)
#space - O(1)