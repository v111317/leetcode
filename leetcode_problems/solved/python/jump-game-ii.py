#https://leetcode.com/problems/jump-game/description

# You are given an integer array nums. You are initially positioned at the array's first index, 
# and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.
from typing import List

class Solution:
    
    def calCost(self, nums, n, costArr):
        if n == len(nums)-1:
            return 0
        
        if costArr[n]!=-1:
            return costArr[n]
        
        cost = []
        #print(n, nums[n])
        for i in range(1, nums[n]+1):
            #print(nums[n], " calling: ", nums[n+i])
            if n+i < len(nums):
                cost.append(1+ self.calCost(nums, n+i, costArr))
        # print(" => ", cost)
        # print("\n")
        if len(cost)!=0:
            costArr[n] = min(cost)
        else:
            costArr[n] = float('+inf')
        
        return costArr[n]
    
    def jump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return 0
        costArr = [-1] * len(nums)
        #print(costArr)
        self.calCost(nums, 0, costArr)
        #print(costArr)
        return costArr[0]
        
sol1 = Solution()
print(sol1.jump([2,3,0,1,4]))
print(sol1.jump([2,3,1,1,4]))
print(sol1.jump([3,2,1,0,4]))
print(sol1.jump([2,0,0]))
print(sol1.jump([2,1]))
print(sol1.jump([5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]))
print(sol1.jump([0]))