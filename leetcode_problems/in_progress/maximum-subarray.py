#https://leetcode.com/problems/maximum-subarray/description

#Given an integer array nums, 
# find the subarray with the largest sum, and return its sum.
from typing import List

class Solution:
    #time limit exceeded
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        
        s = 0
        maxSum = float('-inf')
        i = 0
        j = 0
        while i < len(nums):
            s = nums[i]
            maxSum = max(s, maxSum)
            j = i+1
            while j < len(nums):
                s += nums[j]
                maxSum = max(s, maxSum)
                j += 1
            i += 1
        maxSum = max(s, maxSum)
        return maxSum 
    
    def maxSubArray2(self, nums: List[int]) -> int:
        a = 1
        
sol1 = Solution()
print(sol1.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  
print(sol1.maxSubArray([5,4,-1,7,8]))  
print(sol1.maxSubArray([-2,1]))  
print(sol1.maxSubArray([-2,-1]))  
print(sol1.maxSubArray([-1,-2]))  
      

#time - 
#space -             
        
        
        
#time -
#space -