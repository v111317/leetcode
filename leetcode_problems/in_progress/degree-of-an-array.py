#https://leetcode.com/problems/degree-of-an-array/description/

# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum 
# frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, 
# that has the same degree as nums.
from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return 1
            
        #create hashmap 
        numMap = {}
        idxMap = {}
        for i, num in enumerate(nums):
            if num in numMap:
                numMap[num] += 1
                idxMap[num][1] = i
            else:
                numMap[num] = 1
                idxMap[num] = [i, i]
        
        #find the most frequent element
        values = list(numMap.values())
        keys = list(numMap.keys())
        maxValue = max(values)
        
        #find the min and max index for the most frequent
        minLen = float('+inf')
        for num in numMap:
            if numMap[num] == maxValue:
                minLen = min(minLen, idxMap[num][1]-idxMap[num][0]+1)
        
        return minLen
    
sol1 = Solution()
# print(sol1.findShortestSubArray([1,2,2,3,1]))
print(sol1.findShortestSubArray([1,2,1,1,2,3,4,2]))