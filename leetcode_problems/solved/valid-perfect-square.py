#https://leetcode.com/problems/valid-perfect-square/description/

# Given a positive integer num, return true if num is a perfect square or false otherwise.

# A perfect square is an integer that is the square of an integer. 
# In other words, it is the product of some integer with itself.

# You must not use any built-in library function, such as sqrt.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num == 1:
            return True
        
        n = num
        while pow(n, 2)>num:
            n = n//2
            print(n)
        
        for i in range(n, num):
            print(i)
            if pow(i, 2)==num:
                return True
            
            if pow(i, 2) > num:
                return False

sol1 = Solution()
print(sol1.isPerfectSquare(1))
print(sol1.isPerfectSquare(3))
print(sol1.isPerfectSquare(4))
print(sol1.isPerfectSquare(14))
print(sol1.isPerfectSquare(16))
print(sol1.isPerfectSquare(1331))

#time - O(logn)
#space - O(1)