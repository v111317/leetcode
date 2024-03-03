#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
# find two numbers such that they add up to a specific target number. 
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        start = 0
        end = len(numbers) - 1
        while start < end:
            sumNum = numbers[start] + numbers[end]
            
            if sumNum==target:
                return [start+1, end+1]
            elif sumNum > target:
                end -= 1
            else:
                start += 1

sol1 = Solution()
print(sol1.twoSum([2,7,11,15], 9))
print(sol1.twoSum([-1, 0], -1))

#time - O(n)
#space - O(1)
