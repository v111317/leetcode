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
    #time limit exceeded
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)==0:
            return 0
        
        if len(nums)<=2:
            return max(nums)
        
        robbingFirstHouse = nums[0] + self.rob(nums[2:len(nums)])
        robbingSecondHouse = nums[1] + self.rob(nums[3:len(nums)])
        
        return max(robbingFirstHouse, robbingSecondHouse)
            
sol1 = Solution()
# print(sol1.rob([1,2,3,1]))
#print(sol1.rob([2,7,9,3,1]))
#print(sol1.rob([2,1,1,2]))

#time - 
#space - 