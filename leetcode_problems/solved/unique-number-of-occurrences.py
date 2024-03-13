#https://leetcode.com/problems/unique-number-of-occurrences/description/

# Given an array of integers arr, return true if the number of occurrences of each value in 
# the array is unique or false otherwise.
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numMap = {}
        for num in arr:
            if num in numMap:
                numMap[num] += 1
            else:
                numMap[num] = 1
        
        values = list(numMap.values())
        if len(values)==len(set(values)):
            return True
        else:
            return False

sol1 = Solution()
print(sol1.uniqueOccurrences([1,2,2,1,1,3]))
print(sol1.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
print(sol1.uniqueOccurrences([1,2]))
