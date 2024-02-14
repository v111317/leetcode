from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numMap = {}
        for n in nums:
            if n in numMap:
                numMap[n] += 1
            else:
                numMap[n] = 1
    
        num = [i for i in numMap.keys() if numMap[i]==1]
        
        return num[0]
    
    def singleNumber2(self, nums: List[int]) -> int:
        xor = 0
        for n in nums:
            xor = xor ^ n
        
        return xor
    
    
sol1 = Solution()
print(sol1.singleNumber2([4,1,2,1,2]))

#time - O(n)
#space - O(n)