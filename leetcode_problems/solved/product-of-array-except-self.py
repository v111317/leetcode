#https://leetcode.com/problems/product-of-array-except-self/description/

# Given an integer array nums, return an array answer such that answer[i] 
# is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProd = [1 for i in range(len(nums))]
        suffixProd = [1 for i in range(len(nums))]
        
        for idx, num in enumerate(nums):
            if idx == 0:
                prefixProd[idx] = 1
            else:
                prefixProd[idx] = nums[idx-1] * prefixProd[idx-1]
        
        for idx in range(len(nums)-1, -1, -1):
            
            if idx == len(nums)-1:
                suffixProd[idx] = 1
            else:
                suffixProd[idx] = nums[idx+1] * suffixProd[idx+1]
        
        result = []
        for i in range(len(nums)):
            result.append(prefixProd[i] * suffixProd[i])
        
        return result


sol1 = Solution()
print(sol1.productExceptSelf([1,2,3,4]))
print(sol1.productExceptSelf([-1,1,0,-3,3]))

#time - O(n)
#space - O(n)