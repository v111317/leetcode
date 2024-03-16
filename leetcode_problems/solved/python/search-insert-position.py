#https://leetcode.com/problems/search-insert-position/description/

# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        mid = int(end/2)
        
        while end-start>1:
            
            if target < nums[mid]:
                end = mid
            elif target > nums[mid]:
                start = mid
            else:
                return mid    
            mid = int((start+end)/2)
        
        if nums[mid] == target:
            return mid
        
        if target < nums[start]:
            return start
        elif target > nums[end]:
            return end+1
        else:
            return end
          
    
sol1 = Solution()
print(sol1.searchInsert([1, 3, 5, 6], 3))
print(sol1.searchInsert([1, 3, 5, 6], 2))
print(sol1.searchInsert([1, 3, 5, 6], 0))
print(sol1.searchInsert([1, 3, 5, 6], 7))
print(sol1.searchInsert([1], 0))
print(sol1.searchInsert([1, 3], 1))
print(sol1.searchInsert([1, 3], 3))

#time - O(logn)
#space - O(1)