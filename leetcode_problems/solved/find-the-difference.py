class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        if len(s)==0:
            return t
        
        letterMap = {}
        for letter in t:
            if letter in letterMap:
                letterMap[letter] += 1
            else:
                letterMap[letter] = 1
        
        for letter in s:
            if letter in letterMap:
                letterMap[letter] -= 1

        for key, value in letterMap.items():
            if value==1:
                return key
            
sol1 = Solution()
print(sol1.findTheDifference("abcd", "abcde"))
print(sol1.findTheDifference("", "a"))
print(sol1.findTheDifference("a", "aa"))

#time - O(n)
#space - O(n)