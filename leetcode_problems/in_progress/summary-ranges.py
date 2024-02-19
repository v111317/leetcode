#https://leetcode.com/problems/summary-ranges/description/

# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b

from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        ranges = []
        startIdx = 0
        endIdx = 0
        for endIdx in range(len(nums)):

            if nums[endIdx] - nums[startIdx]<=1:
                continue
            else:
                if nums[startIdx] == nums[endIdx-1]:
                    ranges.append(str(nums[startIdx]))
                else:
                    ranges.append(str(nums[endIdx-1]) + "->" + str(nums[startIdx]))
                startIdx = endIdx
                
        
        # if startIdx < len(nums):
        #     ranges.append(str(nums[startIdx]))        
        return ranges
            
sol1 = Solution()
print(sol1.summaryRanges([0,1,2,4,5,7]))
print(sol1.summaryRanges([0,2,3,4,6,8,9]))

#time - 
#space - 