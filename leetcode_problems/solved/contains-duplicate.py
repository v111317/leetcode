#https://leetcode.com/problems/contains-duplicate/description/

#Given an integer array nums, return true 
# if any value appears at least twice in the array, 
# and return false if every element is distinct.

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

sol1 = Solution()
print(sol1.containsDuplicate([1,2,3,1]))
print(sol1.containsDuplicate([1,2,3,5]))

#time - O(n)
#space- O(n)
                
                