#https://leetcode.com/problems/contains-duplicate-ii/description/?envType=study-plan-v2&envId=top-interview-150

# Given an integer array nums and an integer k, 
# return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

#revise
from typing import List

class Solution:
    #Time Limit Exceeded
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        if len(nums)<=1 or k==0:
            return False
        
        for i in range(len(nums)):
            for j in range(i+1, i+k+1):
                
                if j == len(nums):
                    break
                
                if nums[i]==nums[j]:
                    return True
        
        return False
    
    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        
        numMap = {}
        for idx, num in enumerate(nums):
            if num in numMap:
                if idx - numMap[num] <= k:
                    return True
            numMap[num] = idx
                    
        return False
    
sol1 = Solution()
print(sol1.containsNearbyDuplicate2([1,2,3,1], 2))
print(sol1.containsNearbyDuplicate2([1,0,1,1], 1))
print(sol1.containsNearbyDuplicate2([1,2,3,1,2,3], 2))
print(sol1.containsNearbyDuplicate2([99,99], 2))
print(sol1.containsNearbyDuplicate2([1, 2], 2))
print(sol1.containsNearbyDuplicate2([1,2,3,4,5,6,7,8,9,9], 3))


#solution 1
#time - O(n*n)
#space - O(1)

#solution 2
#time - O(n)
#space - O(n)