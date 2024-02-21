#https://leetcode.com/problems/maximum-product-of-three-numbers/description/

#Given an integer array nums, find three numbers whose product is maximum 
#and return the maximum product.

from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        maxProduct = nums[0] * nums[1] * nums[2]
        
        n = len(nums)
        if n==3:
            return maxProduct
        nums.sort()
        
        return max(nums[n-1]*nums[n-2]*nums[n-3], nums[n-1]*nums[0]*nums[1])
        

sol1 = Solution()
print(sol1.maximumProduct([1,2,3,4])) 
print(sol1.maximumProduct([8,4,3,9,2,8,1,6]))     
print(sol1.maximumProduct([-100,-98,-1,2,3,4]))     

            
            

#time - O(1)
#space - O(1)