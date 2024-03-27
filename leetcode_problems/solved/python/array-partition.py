#https://leetcode.com/problems/array-partition/description/

# Given an integer array nums of 2n integers, group these integers into n pairs 
# (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. 
# Return the maximized sum.
from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums) // 2
        # print

        # i = len(nums)-1
        sumNums = 0
        #print(i)
        for i in range(0, len(nums), 2):
            #print(i)
            sumNums += nums[i]
            
        return sumNums

sol1 = Solution()
# print(sol1.arrayPairSum([1,4,3,2]))
print(sol1.arrayPairSum([6,2,6,5,1,2]))
