#https://leetcode.com/problems/rotate-array/description

# Given an integer array nums, rotate the array to the right by k steps, 
# where k is non-negative.
from typing import List

class Solution:
    #time limit exceeded
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        numLen = len(nums)
        
        if numLen==1 or (k>=numLen and numLen%k==0):
            return nums
        
        count = 0
        while count != k:
            j = 1
            temp = nums[0]
            while j < numLen+1:
                idx = j
                if idx >= numLen:
                    idx %= numLen
                temp2 = temp
                temp = nums[idx]
                nums[idx] = temp2
                j += 1
            count += 1
            
        return nums
    
    def rotate2(self, nums: List[int], k: int) -> None:
        numLen = len(nums)
        
        if k==0 or numLen==1 or (k>=numLen and numLen%k==0):
            return nums
        if k>numLen:
            k = k%numLen
        
        partitionIdx = numLen-k
        count = 0
        i = 0
        while count < partitionIdx//2:
            temp = nums[i]
            nums[i] = nums[partitionIdx-i-1]
            nums[partitionIdx-i-1] = temp
            i += 1
            count += 1
        
        count = 0
        i = partitionIdx
        j = numLen - 1
        while count < k//2:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1
            count += 1
        
        for i in range(numLen//2):
            temp = nums[i]
            nums[i] = nums[numLen-i-1]
            nums[numLen-i-1] = temp
        
        return nums
        
sol1 = Solution()
#print(sol1.rotate2([1,2,3], 2))
print(sol1.rotate2([1,2,3,4,5,6,7], 3))
print(sol1.rotate2([-1,-100,3,99], 2))
print(sol1.rotate2([1,2,3,4,5,6], 11))

#time - O(n)
#space - O(1)




#time - 
#space - 