#https://leetcode.com/problems/valid-palindrome-ii/description/

# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

class Solution:
    
    def isPalindrome(self, s):
        for i in range(len(s)//2):
            if s[i]==s[len(s)-1-i]:
                continue
            else:
                return False
        return True
    
    #time limit exceeded
    def validPalindrome(self, s: str) -> bool:
        isPalin = self.isPalindrome(s)
        
        if isPalin:
            return True
        else:
            for i in range(len(s)):
                newStr = s[0:i] + s[i+1:len(s)]
                isPalin = self.isPalindrome(newStr)
                if isPalin:
                    return True
        return False
    
    def validPalindrome2(self, s: str) -> bool:
        isPalin = self.isPalindrome(s)
        
        if isPalin:
            return True
        else:
            for i in range(len(s)//2):
                if s[i]==s[len(s)-1-i]:
                    continue
                else:
                    break
            newStr = s[i:len(s)-i]
            if self.isPalindrome(newStr[1:]) or self.isPalindrome(newStr[0:len(newStr)-1]):
                return True
            else:
                return False

        
    
    
sol1 = Solution()
print(sol1.validPalindrome2("abca"))
print(sol1.validPalindrome2("aba"))
print(sol1.validPalindrome2("abc"))