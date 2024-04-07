#https://leetcode.com/problems/find-the-difference-of-two-arrays/description/

# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.
from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        numMap1 = {}
        numMap2 = {}
        
        nums1Distinct = []
        nums2Distinct = []
        
        for num in nums1:
            numMap1[num] = 1
        
        for num in nums2:
            numMap2[num] = 1
            
        for num in nums1:
            if num not in numMap2:
                nums1Distinct.append(num)
        
        for num in nums2:
            if num not in numMap1:
                nums2Distinct.append(num)

        return [nums1Distinct, nums2Distinct]
    
sol1 = Solution()
print(sol1.findDifference([1,2,3], [2,4,6]))