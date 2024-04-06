#https://leetcode.com/problems/search-in-rotated-sorted-array/description/

# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, 
# or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1: 
            if nums[0]==target:
                return 0
            else:
                return -1 
            
        start = 0
        end = len(nums)-1
        
        while start <= end:
            mid = (start+end)//2
            print(nums[start], nums[mid], nums[end])
            
            if nums[start]==target:
                return start
            if nums[end]==target:
                return end
            
            if target < nums[mid]:
                if target > nums[start]:
                    end = mid - 1
                else:
                    start = mid + 1
                continue
            elif target > nums[mid]:
                if target < nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
                continue
            else:
                return mid
                
        return -1

sol1 = Solution()
# print(sol1.search([4,5,6,7,0,1,2], 0))
# print(sol1.search([4,5,6,7,0,1,2], 6))        
print(sol1.search([4,5,6,7,8,1,2,3], 8))        
        
#time - 
#space - 
