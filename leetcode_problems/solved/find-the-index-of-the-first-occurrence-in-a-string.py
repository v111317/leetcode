#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except:
            return -1
    
    def strStr2(self, haystack: str, needle: str) -> int:
        
        for i in range(len(haystack)-len(needle)+1):
            matchedChar = 0
            k = i
            for j in range(len(needle)):
                if needle[j]==haystack[k]:
                    matchedChar += 1
                    k += 1
                else:
                    break
            if matchedChar==len(needle):
                return i  
        
        return -1  
sol1 = Solution()
print(sol1.strStr2("sadbutsad", "sad"))
print(sol1.strStr2("leetcode", "leeto"))

#solution1
#time - O(n) #index is O(n) https://stackoverflow.com/questions/5913671/complexity-of-list-indexx-in-python
#space - O(1)

#solution2
#time - O(n*m)
#space - O(1)