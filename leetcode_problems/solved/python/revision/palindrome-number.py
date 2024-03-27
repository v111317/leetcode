#https://leetcode.com/problems/palindrome-number/description/

#Given an integer x, return true if x is a palindrome, and false otherwise.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        cloneNum = 0
        num = x
        while x != 0:
            cloneNum *= 10
            cloneNum += x % 10
            
            x /= 10
            x = int(x)
            #print(cloneNum)
        
        return cloneNum == num

    #reverse half number
    def isPalindrome(self, x: int) -> bool:
        a = 1

sol1 = Solution()
print(sol1.isPalindrome(252))

#time log n
#space O(1)