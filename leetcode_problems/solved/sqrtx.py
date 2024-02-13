import math

class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        mid = (start + end)/2
        
        while abs(mid*mid-x)>0.001:
            if mid * mid > x:
                end = mid
            else:
                start = mid
            mid = (start+end)/2
        
        pos1 = int(mid)
        pos2 = pos1 + 1
        
        if pos2*pos2 == x:
            return pos2
        else:
            return pos1

sol1 = Solution()
print(sol1.mySqrt(9))
print(sol1.mySqrt(8))

print(sol1.mySqrt(49))
print(sol1.mySqrt(59049))
print(sol1.mySqrt(1))

#time O(logn)
#space O(1)
               