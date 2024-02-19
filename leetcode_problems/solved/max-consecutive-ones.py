from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        countOnes = 0
        
        for i in range(len(nums)):
            
            if nums[i] == 1:
                countOnes += 1
            if nums[i]==0 or i==len(nums)-1:
                if countOnes > max:
                    max = countOnes
                countOnes = 0
        return max

sol1 = Solution()
print(sol1.findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(sol1.findMaxConsecutiveOnes([1,0,1,1,0,1]))