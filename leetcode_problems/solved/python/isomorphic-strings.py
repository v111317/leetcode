#https://leetcode.com/problems/isomorphic-strings/description/

# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        letterMap = {}
        
        for idx, letter in enumerate(s):
            if letter in letterMap:
                if letterMap[letter]!=t[idx]:
                    return False
            else:
                if t[idx] in letterMap.values():
                    return False
                letterMap[letter] = t[idx]
                
        
        return True
                
            
            
sol1 = Solution()
# print(sol1.isIsomorphic("paper", "title"))
# print(sol1.isIsomorphic("egg", "ada"))
print(sol1.isIsomorphic("badc", "baba"))

#time - O(n)
#space - O(1)
