from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = 1
        numMap = {}
        for n in nums:
            if n in numMap and numMap[n]==1:
                return True
            else:
                numMap[n] = 1
                
        return False

sol1 = Solution()
print(sol1.containsDuplicate([1,2,3,1]))

#time - O(n)
#space- O(n)
                
                