from typing import List
import math

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        startIdx = 0
        endIdx = len(nums) - 1
        midIdx = math.ceil(endIdx/2)
        
        while midIdx < endIdx:
            if nums[startIdx]==target:
                return startIdx
            elif nums[endIdx]==target:
                return endIdx
            elif nums[midIdx]==target:
                return midIdx
                
            if target < nums[midIdx]:
                endIdx = midIdx
                midIdx = math.ceil((startIdx+midIdx)/2)
            elif target > nums[midIdx]:
                startIdx = midIdx
                midIdx = math.ceil((midIdx+endIdx)/2)
        
        if target > nums[midIdx]:
            return midIdx+1
        elif target < nums[midIdx]:
            return midIdx
                    
          
    
sol1 = Solution()
print(sol1.searchInsert([1, 3, 5, 6], 3))
print(sol1.searchInsert([1, 3, 5, 6], 2))
print(sol1.searchInsert([1, 3, 5, 6], 0))