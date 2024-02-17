class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        letterMap = {}
        for letter in t:
            a = 1