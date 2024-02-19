#https://leetcode.com/problems/maximum-product-of-three-numbers/description/

#Given an integer array nums, find three numbers whose product is maximum 
#and return the maximum product.

from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        maxProduct = nums[0] * nums[1] * nums[2]
        
        if len(nums)==3:
            return maxProduct
        
        numList = nums[0:3]
        minNum = min(numList)
        minIdx = numList.index(minNum)
            
        for i in range(3, len(nums)):
            newProduct = (maxProduct/minNum) * nums[i]
            if newProduct > maxProduct:
                maxProduct = newProduct
                numList[minIdx] = nums[i]
                minNum = min(numList)
                minIdx = numList.index(minNum)
        return int(maxProduct)
    

sol1 = Solution()
print(sol1.maximumProduct([1,2,3,4])) 
print(sol1.maximumProduct([8,4,3,9,2,8,1,6]))     
print(sol1.maximumProduct([-100,-98,-1,2,3,4]))     

            
            

#time - 
#space - 