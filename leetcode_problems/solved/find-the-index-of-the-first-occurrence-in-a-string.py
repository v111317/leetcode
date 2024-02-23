#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except:
            return -1
        
sol1 = Solution()
print(sol1.strStr("leetcode", "leeto"))

#time - O(n) #index is O(n) https://stackoverflow.com/questions/5913671/complexity-of-list-indexx-in-python
#space - O(1)