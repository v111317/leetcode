#https://leetcode.com/problems/backspace-string-compare/description/

# Given two strings s and t, return true if they are equal when both are typed 
# into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

#revise
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        backspaceCount = 0
        finalStr1 = ""
        i = len(s)-1
        while i >= 0:
            if s[i]=='#':
                backspaceCount += 1
            else:
                if backspaceCount == 0:
                    finalStr1 += s[i]
                else:
                    backspaceCount -= 1
            i -= 1
        
        backspaceCount = 0
        finalStr2 = ""
        i = len(t)-1
        while i >= 0:
            if t[i]=='#':
                backspaceCount += 1
            else:
                if backspaceCount == 0:
                    finalStr2 += t[i]
                else:
                    backspaceCount -= 1
            i -= 1
        #print(finalStr1, finalStr2)
        return finalStr1==finalStr2

sol1 = Solution()
print(sol1.backspaceCompare("ac#d", "ab#d"))
print(sol1.backspaceCompare("ac##d", "ab#d"))
print(sol1.backspaceCompare("ac##", "a#b#"))
print(sol1.backspaceCompare("a#c", "c"))
            
        

#time - O(n)
#space - O(n)