#https://leetcode.com/problems/palindrome-number/description/

# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        num = str(x)
        lenStr = len(num)
        
        for i in range(lenStr//2):
            if num[i]!=num[lenStr-1-i]:
                return False
        
        return True

    def isPalindrome2(self, x: int) -> bool:
        cloneNum = 0
        num = x
        while x != 0:
            cloneNum *= 10
            cloneNum += x % 10
            
            x /= 10
            x = int(x)
            #print(cloneNum)
        
        return cloneNum == num
        
sol1 = Solution()
print(sol1.isPalindrome(121))
print(sol1.isPalindrome(-121))
print(sol1.isPalindrome(10))

#solution1
#time - O(k) // k = no. of digits
#space - O(k)

#solution2
#time - O(k) // k = no. of digits
#space - O(1)
 