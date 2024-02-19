#https://leetcode.com/problems/third-maximum-number/description/

# Given an integer array nums, return the third distinct maximum number in this array. 
# If the third maximum does not exist, return the maximum number.

from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        numMap = {}
        for num in nums:
            if num not in numMap:
                numMap[num] = 1
        keys = list(numMap.keys())
        
        if len(keys)<=2:
            return max(keys)
        
        keys.sort()
        return keys[len(keys)-3]

    def thirdMax2(self, nums: List[int]) -> int:
        rankTable = [float('-inf'), float('-inf'), float('-inf')]
        
        for num in nums:
            if num > 1

sol1 = Solution()
print(sol1.thirdMax([3,2,1]))
print(sol1.thirdMax([2,1]))
print(sol1.thirdMax([2,2,1,1]))

#solution 1
#time - O(nlogn)
#space - O(n)