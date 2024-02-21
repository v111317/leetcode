#https://leetcode.com/problems/house-robber/description/

# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed, the only constraint stopping you 
# from robbing each of them is that adjacent houses have security systems connected 
# and it will automatically contact the police if two adjacent houses were broken into
# on the same night.

# Given an integer array nums representing the amount of money of each house, 
# return the maximum amount of money you can rob tonight without alerting the police.

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        max = 0
        i = 0
        #sum = nums[i] + self.rob(nums[i+2])
            
sol1 = Solution()
print(sol1.rob([1,2,3,1]))
print(sol1.rob([2,7,9,3,1]))
print(sol1.rob([2,1,1,2]))

#time - 
#space - 