#https://leetcode.com/problems/intersection-of-two-arrays/description/

#Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must be unique and you may return the result in any order.

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numMap = {}
        commonNums = set()
        for n in nums1:
            if n not in numMap:
                numMap[n] = 1
                
        for n in nums2:
            if n in numMap:
                commonNums.add(n)
                
        return list(commonNums)

sol1 = Solution()
print(sol1.intersection([1,2,2,1], [2,2]))
print(sol1.intersection([4,9,5], [9,4,9,8,4]))

#time - O(n)
#space - O(n)