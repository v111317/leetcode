#https://leetcode.com/problems/max-pair-sum-in-an-array/description/

# You are given a 0-indexed integer array nums. You have to find the maximum sum of a pair of numbers from nums such 
# that the maximum digit in both numbers are equal.

# Return the maximum sum or -1 if no such pair exists.
from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        maxDigitMap = {}
        for num in nums:
            numStr = str(num)
            maxDigit = max(numStr)
            if maxDigit in maxDigitMap:
                maxDigitMap[maxDigit].append(num)
            else:
                maxDigitMap[maxDigit] = [num]
        
        maxSum = -1
        for key, numList in maxDigitMap.items():
            numList.sort(reverse=True)
            if len(numList) >= 2:
                maxSum = max(maxSum, numList[0]+numList[1])
        
        return maxSum

sol1 = Solution()
print(sol1.maxSum([51,71,17,24,42]))  
print(sol1.maxSum([1,2,3,4]))  
        
#time - O(n)
#space - O(n)
