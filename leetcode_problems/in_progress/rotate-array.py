from typing import List

#https://leetcode.com/problems/rotate-array/description

# Given an integer array nums, rotate the array to the right by k steps, 
# where k is non-negative.
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        
        if n==1:
            return nums
        
        if n%k==0:
            return nums
        count = 0
        i = 0
        while count != n:
            #print(nums[(i+k)%n], nums[i])
            i = (i+k)%n
            temp = nums[i]
            nums[i] = nums[i]
            count += 1
            
            #print(nums)
            
        return nums
sol1 = Solution()
print(sol1.rotate([1,2,3,4,5,6,7], 3))
#time - 
#space - 