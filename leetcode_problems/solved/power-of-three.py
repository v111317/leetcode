#https://leetcode.com/problems/power-of-three/description/

# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n!=0:
            if n==1:
                return True
            
            if n%3==0:
                n = int(n/3)
            else:
                return False

sol1 = Solution()
print(sol1.isPowerOfThree(27))
print(sol1.isPowerOfThree(28))

#time - O(log to base 3 of n)
#space - O(1)
