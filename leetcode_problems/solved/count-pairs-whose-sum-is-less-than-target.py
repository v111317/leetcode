#https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

# Given a 0-indexed integer array nums of length n and an integer target, 
# return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        
        i = 0
        count = 0
        while i < len(nums)-1:
            j = i + 1
            while j < len(nums): 
                if nums[i] +nums[j] < target:
                    count += 1
                elif nums[i]+nums[j]>=target:
                    break
                j += 1
            i += 1
        return count

sol1 = Solution()
print(sol1.countPairs([-1,1,2,3,1], 2))
print(sol1.countPairs([-6,2,5,-2,-7,-1,3], -2))


#time - O(n*n)
#space - O(1)
        