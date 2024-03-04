#https://leetcode.com/problems/duplicate-zeros/description/

#Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written. 
# Do the above modifications to the input array in place and do not return anything.
from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if len(arr)==1:
            return arr
        
        zeroFinder = -1
        i = 0
        while i < len(arr):
            if arr[i]==0:
                zeroFinder = i
                j = len(arr) - 1
                while j > zeroFinder:
                    arr[j] = arr[j-1]
                    j -= 1
                if zeroFinder < len(arr)-1:
                    arr[zeroFinder+1] = 0
                i = i+2
            else:
                i += 1
        return arr

sol1 = Solution()        
print(sol1.duplicateZeros([1,0,2,3,0,4,5,0]))
print(sol1.duplicateZeros([0,4,1,0,0,8,0,0,3]))


#time - O(n*n)
#space - O(1)