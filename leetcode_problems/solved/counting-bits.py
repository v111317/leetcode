#https://leetcode.com/problems/counting-bits/description/

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
# ans[i] is the number of 1's in the binary representation of i.
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        result = [0]
        for n in range(1, n+1):
            onesCount = 0
            while n!=0:
                onesCount += n%2
                n = n//2
            result.append(onesCount)
        return result
        
sol1 = Solution()
print(sol1.countBits(5))     
print(sol1.countBits(2)) 
print(sol1.countBits(1)) 
      
#time - O(n*logn)
#space - O(1)