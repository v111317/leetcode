#https://leetcode.com/problems/maximum-subarray/description

#Given an integer array nums, 
# find the subarray with the largest sum, and return its sum.
from typing import List

class Solution:
    #time limit exceeded
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        
        s = 0
        maxSum = float('-inf')
        i = 0
        j = 0
        while i < len(nums):
            s = nums[i]
            maxSum = max(s, maxSum)
            j = i+1
            while j < len(nums):
                s += nums[j]
                maxSum = max(s, maxSum)
                j += 1
            i += 1
        maxSum = max(s, maxSum)
        return maxSum 
    
    #time limit exceeded
    def maxSubArray2(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        sumArr = []
        total = 0
        sumMax = float('-inf')
        start = 0
        end = 0
        for i, num in enumerate(nums):
            total += num
            if total > sumMax:
                end = i
                sumMax  = total
            sumArr.append(total)
        
        for i in range(1, len(nums)):
            j = i
            start = i
            while j < len(sumArr):
                sumArr[j] -= nums[i-1]
                if sumArr[j] > sumMax:
                    end = j
                    sumMax = sumArr[j]
                j += 1
        return sumMax

    def maxSubArray3(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = float('-inf')
        
        for num in nums:
            currSum += num
            if currSum > maxSum:
                maxSum = currSum
            
            if currSum < 0 :
                currSum = 0
        
        return maxSum
        
sol1 = Solution()
print(sol1.maxSubArray3([-2,1,-3,4,-1,2,1,-5,4]))  
print(sol1.maxSubArray3([5,4,-1,7,8]))  
print(sol1.maxSubArray3([-2,1]))  
print(sol1.maxSubArray3([-2,-1]))  
print(sol1.maxSubArray3([-1,-2]))  
print(sol1.maxSubArray3([1]))  
      

#time - 
#space -             
        
        
        
#time -
#space -