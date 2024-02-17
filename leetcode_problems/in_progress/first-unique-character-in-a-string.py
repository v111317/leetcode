class Solution:
    def firstUniqChar(self, s: str) -> int:
        letterMap = {}
        minIdx = -1
        
        for idx, letter in enumerate(s):
            if letter in letterMap:
                letterMap[letter] = -1
            else:
                letterMap[letter] = idx
        
        print(letterMap)
        if letterMap.values().count(-1)==len(letterMap.values()):
            return -1
        else:
            for i in letterMap.values():
                if i==-1:
                    continue
                else:
                    if i>1:
                        a = 1
        return min(letterMap.values())
    
sol1 = Solution()
print(sol1.firstUniqChar("leetcode"))
print(sol1.firstUniqChar("loveleetcode"))
print(sol1.firstUniqChar("aabb"))
        
        