#https://leetcode.com/problems/jump-game/description

# You are given an integer array nums. You are initially positioned at the array's first index, 
# and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        
        lastCheckpoint = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if nums[i]>=lastCheckpoint-i:
                lastCheckpoint = i
                
        if lastCheckpoint == 0:
            return True
        else:
            return False
        
sol1 = Solution()
print(sol1.canJump([2,3,1,1,4]))
print(sol1.canJump([3,2,1,0,4]))
print(sol1.canJump([2,0,0]))