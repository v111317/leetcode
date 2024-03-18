#https://leetcode.com/problems/repeated-substring-pattern/description/

# Given a string s, check if it can be constructed by taking a substring of it 
# and appending multiple copies of the substring together.

class Solution:
    #time limit exceeded
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s)==1:
            return False
        lenStr = len(s)
        i = 0
        while i < lenStr//2:
            subStr = s[0:i+1]
            # print(subStr)
            lenSubStr = i+1
            if lenStr % lenSubStr == 0:
                count = lenStr // lenSubStr
                if subStr*count == s:
                    return True
            i += 1
        return False

sol1 = Solution()
print(sol1.repeatedSubstringPattern("abab"))
print(sol1.repeatedSubstringPattern("ababba"))
print(sol1.repeatedSubstringPattern("abcabcabcabc"))
print(sol1.repeatedSubstringPattern("abaababaab"))


        
#time -
#space - 