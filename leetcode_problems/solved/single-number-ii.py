#https://leetcode.com/problems/single-number-ii/description/

# Given an integer array nums where every element appears three times except for one, 
# which appears exactly once. Find the single element and return it.

# You must implement a solution with a linear runtime complexity and use only constant extra space.
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(0, 32):
            sumNums = 0
            for num in nums:
                if num < 0:
                    num = num & (2**32-1)
                sumNums += (num >> i) & 1
                
            if sumNums%3==1:
                ans = ans | 1 << i
                if ans >= 2**31:
                    ans -= 2**32
                
        return ans

sol1 = Solution()
# print(sol1.singleNumber([2,2,3,2]))
# print(sol1.singleNumber([0,1,0,1,0,1,99]))
print(sol1.singleNumber([-2,-2,1,1,4,1,4,4,-4,-2]))

            
            
                
        
