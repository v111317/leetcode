#https://leetcode.com/problems/contains-duplicate/description/

#Given an integer array nums, return true 
# if any value appears at least twice in the array, 
# and return false if every element is distinct.

#revise
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numMap = {}
        for n in nums:
            if n in numMap:
                return True
            else:
                numMap[n] = 1
                
        return False
    
    def containsDuplicate2(self, nums: List[int]) -> bool:
        numsAsSet = set(nums)
        if len(numsAsSet) < len(nums):
            return True
        else:
            return False

sol1 = Solution()
print(sol1.containsDuplicate([1,2,3,1]))
print(sol1.containsDuplicate([1,2,3,5]))

#solution 1
#time - O(n)
#space- O(n)
                
#solution 2
#time - O(1)
#space- O(1)
                