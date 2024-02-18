from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        max = len(nums)
        numMap = {}
        missingNums = []
        
        for n in nums:    
            if n not in numMap:
                numMap[n] = 1
        
        for n in range(1, max+1):
            if n not in numMap:
                missingNums.append(n)
        
        return missingNums
        
sol1 = Solution()
print(sol1.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(sol1.findDisappearedNumbers([1, 1]))
print(sol1.findDisappearedNumbers([2, 2]))
print(sol1.findDisappearedNumbers([1, 2]))

#time - O(n)
#space - O(1)