from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        
        while j>=0: 
            if i>=0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
        return nums1
    
sol1 = Solution()
#print(sol1.merge([1,2,3,9,10,0,0,0], 5, [2,5,6], 3))
print(sol1.merge([2,0], 1, [1], 1))