#https://leetcode.com/problems/rotate-string/description/

# Given two strings s and goal, return true if and only if s can become goal after some number of 
# shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        if len(s)!=len(goal):
            return False
        
        for i in range(len(s)):
            count = 0
            #print(i, s[i])
            k = i
            for j in range(len(goal)):
                #print(" => ", j, goal[j])
                
                if goal[j]==s[k]:
                    count += 1
                    k += 1
                    if k>=len(s):
                        k %= len(s)
                else:
                    break
            if count==len(s):
                return True
        
        return False

sol1 = Solution()
print(sol1.rotateString("abcde", "bcdea"))
print(sol1.rotateString("abcde", "bceda"))