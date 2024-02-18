from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        max = 0
        i = 0
        sum = nums[i] + self.rob(nums[i+2]))
            
sol1 = Solution()
print(sol1.rob([1,2,3,1]))
print(sol1.rob([2,7,9,3,1]))
print(sol1.rob([2,1,1,2]))