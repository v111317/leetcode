#https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

# You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose 
# two indices in a string (not necessarily different) and swap the characters at these indices.

# Return true if it is possible to make both strings equal by performing at most one string swap on exactly 
# one of the strings. Otherwise, return false.

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
    

        if len(s1)!=len(s2):
            return False
        if s1==s2:
            return True
        
        letterMap = {}
        mismatchCount = 0
        ch = ''
        swapCh = ''
        idx = -1
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                ch = s1[i]
                swapCh = s2[i]
                idx = i
                break
    
        for i in range(len(s1)):
            if s1[i]!=s2[i] and s1[i]==swapCh:
                newStr = list(s1)
                newStr[idx] = swapCh
                newStr[i] = ch
                newStr = "".join(newStr)
                if newStr==s2:
                    return True
                else:
                    return False
        return False
            
            
                
            
        
sol1 = Solution()
print(sol1.areAlmostEqual("bank", "kanb"))
print(sol1.areAlmostEqual("attack", "defend"))
print(sol1.areAlmostEqual("abcd", "abcd"))
print(sol1.areAlmostEqual("siyolsdcjthwsiplccjbuceoxmpjgrauocx", "siyolsdcjthwsiplccpbuceoxmjjgrauocx"))



#time - O(n)
#space - O(n)