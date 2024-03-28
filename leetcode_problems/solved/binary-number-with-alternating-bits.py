#https://leetcode.com/problems/binary-number-with-alternating-bits/description/

# Given a positive integer, check whether it has alternating bits: namely, 
# if two adjacent bits will always have different values.

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        isZero = False
        if n & 1==0:
            isZero = True
        
        n = n >> 1
        
        while n!=0:
            #print(n, isZero)
            if (n & 1)==0:
                if isZero:
                    return False
                else:
                    isZero = True
            else:
                if not isZero:
                    return False
                else:
                    isZero = False
            n = n >> 1
        return True

sol1 = Solution()
print(sol1.hasAlternatingBits(5))
print(sol1.hasAlternatingBits(7))
print(sol1.hasAlternatingBits(11))

#time - O(logn)
#space - O(1)
            