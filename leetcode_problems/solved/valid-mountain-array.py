#https://leetcode.com/problems/valid-mountain-array/

# Given an array of integers arr, return true if and only if 
# it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        
        i = 1
        countIncreasing = 0
        countDecreasing = 0
        increase = True
        while i < len(arr):
            if arr[i]==arr[i-1]:
                return False
                
            if arr[i] > arr[i-1] :
                if increase:
                    countIncreasing += 1
                    i += 1
                    continue
                else:
                    return False
            
            if arr[i] < arr[i-1]:
                if countDecreasing == 0:
                    increase = False
                    countDecreasing += 1 
                else:
                    countDecreasing += 1 
                    
            i += 1
        
        if not increase and countIncreasing > 0 and countDecreasing > 0:
            return True
        else:
            return False
        
sol1 = Solution()
print(sol1.validMountainArray([0,2,3,4,5,2,1,0]))
print(sol1.validMountainArray([0,6,3,4,5,2,1,0]))
print(sol1.validMountainArray([3,5,5]))
print(sol1.validMountainArray([2,1]))
print(sol1.validMountainArray([0,3,2,1]))
#time - O(n)
#space - O(1)