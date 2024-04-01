#https://leetcode.com/problems/find-peak-element/description/

# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. 
# If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered 
# to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return 0
        
        start = 0
        end = n - 1
        
        while start <= end:
            mid = (start+end)//2
            
            if mid>0 and mid<n-1:
                if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                    return mid