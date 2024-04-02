#https://leetcode.com/problems/find-pivot-index/description/

# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index
# is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are 
# no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        sumNums = sum(nums)

        if n==1: #or sumNums-nums[0]==0:
            return 0
        
        # if sumNums-nums[n-1]==0:
        #     return n-1
        
        leftSum = 0
        rightSum = sumNums
        
        for i in range(n):
            if i > 0:
                leftSum += nums[i-1]
            
            rightSum -= nums[i]
            print(i, leftSum, rightSum)
            if leftSum==rightSum:
                return i
        return -1
    
sol1 = Solution()
# print(sol1.pivotIndex([1,7,3,6,5,6]))
# print(sol1.pivotIndex([1,2,3]))
# print(sol1.pivotIndex([2,1,-1]))
print(sol1.pivotIndex([-1,-1,1,1,0,0]))

