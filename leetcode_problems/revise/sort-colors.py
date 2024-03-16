#https://leetcode.com/explore/learn/card/sorting/694/comparison-based-sorts/4483/

# Given an array nums with n objects colored red, white, or blue, 
# sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return nums
        
        for i in range(len(nums)):
            minNumIdx = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[minNumIdx]:
                   minNumIdx = j
            if minNumIdx!=i:
                temp = nums[i]
                nums[i] = nums[minNumIdx]
                nums[minNumIdx] = temp
        
        return nums
    
    def sortColors2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return nums  
        
        numMap = {0:0, 1:0, 2:0}
        for num in nums:
            numMap[num] += 1
            
        for idx in range(len(nums)):
            if numMap[0] > 0:
                n = 0
                
            elif numMap[1] > 0:
                n = 1
            elif numMap[2] > 0:
                n = 2
            nums[idx] = n
            numMap[n] -= 1
        
        return nums
        
        

sol1 = Solution()
print(sol1.sortColors2([2,0,2,1,0]))