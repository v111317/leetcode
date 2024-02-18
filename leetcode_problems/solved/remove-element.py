from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        idx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1
        return idx    
    
    def removeElement2(self, nums: List[int], val: int) -> int:
        
        count = 0
        for n in nums:
            if n == val:
                count += 1
        
        validNums = len(nums) - count
        j = len(nums)-1
        for i in range(validNums):
            if nums[i] == val:
                while nums[j]==val:
                    j -= 1
                nums[i] = nums[j]
                j -= 1
        return validNums
            
sol1 = Solution()
print(sol1.removeElement([0,1,2,2,3,0,4,2], 2))
print(sol1.removeElement([3,2,2,3], 3))

#time - O(n*n)
#space - O(1)