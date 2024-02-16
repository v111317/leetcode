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
