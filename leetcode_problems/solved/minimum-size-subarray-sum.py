#https://leetcode.com/problems/minimum-size-subarray-sum/description

# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
from typing import List

class Solution:
    #time limit exceeded
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        if target > sum(nums):
            return 0
        
        windowLen = 1
        while windowLen <= len(nums):
            # print(" ======> ", windowLen)
            sumNums = 0
            for i in range(windowLen):
                sumNums += nums[i]
                if sumNums >= target:
                    return windowLen
            # print(windowLen, sumNums)
            # print("=====")
            for i in range(1, len(nums)-windowLen+1):
                sumNums -= nums[i-1]
                sumNums += nums[i+windowLen-1]
                # print(windowLen, sumNums)
                if sumNums >= target:
                    return windowLen
            # print("\n\n")
            windowLen += 1
        return 0
    
    def minSubArrayLen2(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        n = len(nums)
        sumNums = 0
        minWindowLen = float('+inf')
        
        while i < n and j < n:
            sumNums += nums[j]
            # print(i, j, sumNums)
            while sumNums>=target:
                minWindowLen = min(minWindowLen, j-i+1)
                sumNums -= nums[i]
                i += 1
                
            if sumNums < target:
                j += 1
                    
        return minWindowLen
                        

sol1 = Solution()
print(sol1.minSubArrayLen2(7, [2,3,1,2,4,3])) 
# print(sol1.minSubArrayLen(4, [1,4,4]))   
# print(sol1.minSubArrayLen(11, [1,2,3,4,5]))       
