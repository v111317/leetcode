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
    
sol1 = Solution()
print(sol1.firstUniqChar("leetcode"))
print(sol1.firstUniqChar("loveleetcode"))
print(sol1.firstUniqChar("aabb"))

#time - O(n)
#space - O(n)        
        