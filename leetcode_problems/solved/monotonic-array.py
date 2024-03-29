#https://leetcode.com/problems/monotonic-array/description/

# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. 
# An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is monotonic, 
# or false otherwise.

from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        
        countIncreasing = 0
        countDecreasing = 0
        countSame = 0
        
        i = 1
        while i < len(nums):
            if nums[i] > nums[i-1]:
                countIncreasing += 1
            elif nums[i] < nums[i-1]:    
                countDecreasing += 1
            else:
                countSame += 1
        
            if countIncreasing >0 and countDecreasing >0:
                return False
            i += 1
        return True

sol1 = Solution()
print(sol1.isMonotonic([1,2,2,3]))    
print(sol1.isMonotonic([1,3,2]))
print(sol1.isMonotonic([6,5,4,4]))    

#time - O(n)
#space - O(1)