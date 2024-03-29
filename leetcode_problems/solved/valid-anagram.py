class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterMap = {}
        
        if len(s)!=len(t):
            return False
        
        for l in s:
            if l in letterMap:
                letterMap[l] += 1
            else:
                letterMap[l] = 1
        
        for l in t:
            if l in letterMap and letterMap[l]>0:
                letterMap[l] -= 1
            else:
                return False
            
        return True

sol1 = Solution()
print(sol1.isAnagram("anagram", "nagaram"))
print(sol1.isAnagram("ab", "a"))
#print(sol1.isAnagram("rat", "car"))

#time - O(n)
#space - O(n)
            