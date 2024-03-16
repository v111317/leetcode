#https://leetcode.com/problems/first-unique-character-in-a-string/description/

#Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

#revise
class Solution:
    def firstUniqChar(self, s: str) -> int:
        letterMap = {}
        minIdx = 100000
        
        for idx, letter in enumerate(s):
            if letter in letterMap:
                letterMap[letter] = -1
            else:
                letterMap[letter] = idx
         
        for idx in letterMap.values():
            if idx!=-1 and idx < minIdx:
                minIdx = idx 
        
        if sum(1 for n in letterMap.values() if n==-1)==len(letterMap.values()):
            return -1
        else:
            return minIdx
    
    def firstUniqChar2(self, s: str) -> int:
        letterMap = {}
        
        for idx, letter in enumerate(s):
            if letter in letterMap:
                letterMap[letter] += 1
            else:
                letterMap[letter] = 1
         
        for idx, letter in enumerate(s):
            if letterMap[letter] == 1:
                return idx
        return -1
        
    
sol1 = Solution()
print(sol1.firstUniqChar2("leetcode"))
print(sol1.firstUniqChar2("loveleetcode"))
print(sol1.firstUniqChar2("aabb"))

#time - O(n)
#space - O(1)        
        