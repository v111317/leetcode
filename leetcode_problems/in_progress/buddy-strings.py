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
        for idx, letter in enumerate(s):
            if letter == goal:
                a = 1
        
        
#time - 
#space - 