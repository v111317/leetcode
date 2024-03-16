#https://leetcode.com/problems/power-of-four/description/

# Given an integer n, return true if it is a power of four. Otherwise, return false.

# An integer n is a power of four, if there exists an integer x such that n == 4x.

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n==1:
            return True
        if n<0:
            return False
        
        count = 0
        while n%4==0:
            n = int(n/4)
            count += 1
            if n < 4:
                if n == 1:
                    return True
                else:
                    return False   
        if n == -1 and count%2==1:
            return True    
        return False
    
    #recursion
    def isPowerOfFour2(self, n: int) -> bool:
        if n==4 or n==1:
            return True
        
        if n <= 0:
            return False
        
        if n%4==0:
            return self.isPowerOfFour(int(n/4))
        else:
            return False

sol1 = Solution()
print(sol1.isPowerOfFour2(64))
print(sol1.isPowerOfFour2(32))
print(sol1.isPowerOfFour2(15))
print(sol1.isPowerOfFour2(-64))

#time - O(log n to base 4)
#space - O(1)