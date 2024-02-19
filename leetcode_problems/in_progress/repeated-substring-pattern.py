#https://leetcode.com/problems/repeated-substring-pattern/description/

# Given a string s, check if it can be constructed by taking a substring of it 
# and appending multiple copies of the substring together.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        letterMap = {}
        
        if len(s)==1:
            return False
        
        for letter in s:
            if letter in letterMap:
                letterMap[letter] += 1
            else:
                letterMap[letter] = 1
        
        values = list(letterMap.values())
        
        for i in range(len(values)-1):
            if values[i]==values[i+1]:
                continue
            else:
                return False
        return True

sol1 = Solution()
print(sol1.repeatedSubstringPattern("aba"))
print(sol1.repeatedSubstringPattern("ababba"))
        
#time -
#space - 