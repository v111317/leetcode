#https://leetcode.com/problems/sort-array-by-parity/description/

# Given an integer array nums, move all the even integers at the beginning of 
# the array followed by all the odd integers.

# Return any array that satisfies this condition.

from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        i = 0
        j = len(nums) - 1
        
        while i<j:
            if nums[i]%2==1 and nums[j]%2==0:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                i += 1
                j -= 1
            if nums[i]%2==0:
                i += 1
            if nums[j]%2==1:
                j -= 1  
        return nums
        
sol1 = Solution()
print(sol1.sortArrayByParity([3,1,2,4]))
print(sol1.sortArrayByParity([2,1,4,5,6,8,9]))
#time - O(n)
#space - O(1)