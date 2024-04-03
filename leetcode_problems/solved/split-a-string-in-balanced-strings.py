#https://leetcode.com/problems/split-a-string-in-balanced-strings/description/

# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

# Given a balanced string s, split it into some number of substrings such that:

# Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        countBalStr = 0
        countL = 0
        countR = 0
        
        for letter in s:
            if letter == "R":
                countR += 1
            else:
                countL += 1
            
            if countL==countR:
                countBalStr += 1
                countL = 0
                countR = 0
                
        return countBalStr

sol1 = Solution()
print(sol1.balancedStringSplit("RLRRLLRLRL"))
print(sol1.balancedStringSplit("RLRRRLLRLL"))
print(sol1.balancedStringSplit("LLLLRRRR"))
        