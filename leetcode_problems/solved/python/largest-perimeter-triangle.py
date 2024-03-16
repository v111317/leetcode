#https://leetcode.com/problems/largest-perimeter-triangle/description/

# Given an integer array nums, return the largest perimeter of a triangle 
# with a non-zero area, formed from three of these lengths. 
# If it is impossible to form any triangle of a non-zero area, return 0.
from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        j = len(nums) - 1
        
        i = j - 2
        maxPeri = 0
        while i >= 0:
            if (nums[i] + nums[i+1]) > nums[i+2]:
                maxPeri = max(maxPeri, nums[i]+nums[i+1]+nums[i+2])
            j -= 1
            i -= 1
        return maxPeri

sol1 = Solution()
print(sol1.largestPerimeter([2,3,3,6]))
print(sol1.largestPerimeter([1,2,1,10]))

#time - 
#space - 
        
        