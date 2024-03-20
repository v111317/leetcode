#https://leetcode.com/problems/maximum-average-subarray-i/description/

# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
# Any answer with a calculation error less than 10-5 will be accepted.
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumNums = 0
        for i in range(k):
            sumNums += nums[i]
        
        maxSum = sumNums
        
        for i in range(1, len(nums)-k+1):
            sumNums -= nums[i-1]
            sumNums += nums[i+k-1]
            maxSum = max(sumNums, maxSum)
        
        return maxSum/k
    
sol1 = Solution()
print(sol1.findMaxAverage([1,12,-5,-6,50,3], 4))