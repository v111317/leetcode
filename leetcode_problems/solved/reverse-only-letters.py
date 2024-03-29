#https://leetcode.com/problems/reverse-only-letters/description/

# Given a string s, reverse the string according to the following rules:

# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        if len(s)==1:
            return s
        
        i = 0
        j = len(s)-1
        
        revStr = list(s)
        
        while i < j:
            if revStr[i].isalpha() and revStr[j].isalpha():
                temp = revStr[j]
                revStr[j] = revStr[i]
                revStr[i] = temp
                i += 1
                j -= 1
            elif not revStr[i].isalpha():
                i += 1
            elif not revStr[j].isalpha():
                j -= 1
        s = "".join(revStr)
        return s
    
sol1 = Solution()
print(sol1.reverseOnlyLetters("a-bC-dEf-ghIj")) 

        
        
#time - O(n)
#space - O(n)