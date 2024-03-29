#https://leetcode.com/problems/consecutive-characters/description/

# The power of the string is the maximum length of a non-empty substring that contains only one unique character.
# Given a string s, return the power of s.

class Solution:
    def maxPower(self, s: str) -> int:
        if len(s)==1:
            return 1
        start = 0
        end = 0
        count = 0
        maxPower = 0
        while end < len(s):
            if s[start]==s[end]:
                count += 1
                end += 1
            else:
                start += 1
                maxPower = max(maxPower, count)
                count = 0 
        if count > 0:
            return max(maxPower, count)
        return maxPower
           
        
    
sol1 = Solution()
# print(sol1.maxPower("leetcode"))
print(sol1.maxPower("abbcccddddeeeeedcbaaaaaaaa"))

#time - O(n)
#space - O(1)

