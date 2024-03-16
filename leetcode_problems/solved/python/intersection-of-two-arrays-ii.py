#https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numMap = {}
        commonNums = []
        for n in nums1:
            if n not in numMap:
                numMap[n] = 1
            else:
                numMap[n] += 1
                
        for n in nums2:
            if n in numMap and numMap[n]>0:
                commonNums.append(n)
                numMap[n] -= 1
                
        return list(commonNums)

sol1 = Solution()
print(sol1.intersect([1,2,2,1], [2,2]))
print(sol1.intersect([4,9,5], [9,4,9,8,4]))

#time - O(n)
#space - O(n)

# Follow up:

# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that 
# you cannot load all elements into the memory at once?