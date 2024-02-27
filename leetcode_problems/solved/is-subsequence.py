#https://leetcode.com/problems/is-subsequence/description/

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
# of the characters without disturbing the relative positions of the remaining characters. 
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i = 0
        count = len(s)
        
        if count == 0:
            return True
        
        for letter in t:
            if letter == s[i]:
                count -= 1
                i += 1
                if count == 0:
                    return True
        return False

sol1 = Solution()
print(sol1.isSubsequence("abc", "ahbgdc"))
print(sol1.isSubsequence("axc", "ahbgdc"))
print(sol1.isSubsequence("abb", "ahbgdbc"))
print(sol1.isSubsequence("", "ahbgdbc"))

#time - O(n)
#space - O(1)
