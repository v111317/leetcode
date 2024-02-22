#https://leetcode.com/problems/buddy-strings/description/

# Given two strings s and goal, return true if you can swap two letters in s 
# so the result is equal to goal, otherwise, return false.

# Swapping letters is defined as taking two indices i and j (0-indexed) 
# such that i != j and swapping the characters at s[i] and s[j].

# For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) < 2 or len(s)!=len(goal):
            return False
        
        letterMap = {}
        i = 0
        countMismatch = 0
        
        if s==goal:
            
            while i < len(s):
                key = s[i] + goal[i]
                if key not in letterMap:
                    letterMap[key] = 1
                else:
                    return True
                i += 1
            return False
        else :        
            while i < len(s):
                if s[i]!=goal[i]:
                    countMismatch += 1
                    if countMismatch > 2:
                        return False
                    
                    key = s[i] + goal[i]
                    key2 = goal[i] + s[i]
                    if key not in letterMap:
                        
                        letterMap[key] = 1
                        letterMap[key2] = 0
                    else:
                        letterMap[key] += 1
                              
                i += 1
                
            for n in list(letterMap.values()):
                if n == 0:
                    return False
            return True           
    
sol1 = Solution()
print(sol1.buddyStrings("abcd", "cbad"))   
print(sol1.buddyStrings("aba", "aba"))   
print(sol1.buddyStrings("ab", "ba"))  
print(sol1.buddyStrings("aa", "aa"))       
print(sol1.buddyStrings("abcdef", "cbadef"))   
print(sol1.buddyStrings("abcdef", "cbadeg"))    
print(sol1.buddyStrings("abcaa", "abcbb"))    
#time - 
#space - 