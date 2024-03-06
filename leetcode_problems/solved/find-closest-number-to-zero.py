#https://leetcode.com/problems/find-closest-number-to-zero/description/

# Given an integer array nums of size n, return the number with the value closest to 0 in nums. 
# If there are multiple answers, return the number with the largest value.
from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        numMap = {}
        minDist = float('inf')
        for num in nums:
            if abs(num) not in numMap:
                numMap[abs(num)] = [num]
                minDist = min(minDist, abs(num))
            else:
                numMap[abs(num)].append(num)
        
        return max(numMap[minDist])

sol1 = Solution()
print(sol1.findClosestNumber([-4,-2,1,4,8]))
print(sol1.findClosestNumber([2,-1,1]))

#time - O(n)
#space - O(n)                
