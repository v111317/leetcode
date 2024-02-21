#https://leetcode.com/problems/backspace-string-compare/description/

# Given two strings s and t, return true if they are equal when both are typed 
# into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sHashCount = 0
        tHashCount = 0
        
        sLen = len(s)
        tLen = len(t)
        maxLen = max(sLen, tLen)
        sIdx = sLen - 1
        tIdx = tLen - 1
        
        while sIdx >= 0 or tIdx >= 0:
            if sHashCount==0 and tHashCount==0 and s[sIdx]!='#' and t[tIdx]!='#':
                if s[sIdx]!=t[tIdx]:
                    return False
            else:
                if s[sIdx]=='#':
                    sHashCount += 1
                if t[tIdx]=='#':
                    tHashCount += 1
                if sHashCount >= 0 and s[sIdx]!='#':
                    sHashCount -= 1
                if tHashCount >= 0 and t[tIdx]!='#':
                    tHashCount -= 1
            
            if sIdx >= 1:
                sIdx -= 1
            if tIdx >= 1:
                tIdx -= 1
        
        if sIdx == 0 and tIdx == 0:
            return True
        else:
            return False
        

#time - 
#space -