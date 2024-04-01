#https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

# You are given an array of characters letters that is sorted in non-decreasing order, and 
# a character target. There are at least two different characters in letters.

# Return the smallest character in letters that is lexicographically greater than target. 
# If such a character does not exist, return the first character in letters.
from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        n = len(letters)
        if target < letters[0] or target > letters[n-1]:
            return letters[0]
        
        for letter in letters:
            if target < letter:
                return letter
        
        return latters[0]

    def nextGreatestLetter2(self, letters: List[str], target: str) -> str:
        n = len(letters)
        if target < letters[0] or target > letters[n-1]:
            return letters[0]
        
        for i in range(ord(target)+1, 123):
            ch = chr(i)
            if ch in letters:
                return ch
        return letters[0]
    
sol1 = Solution()
print(sol1.nextGreatestLetter2(["c","f","j"], "a"))
print(sol1.nextGreatestLetter2(["c","f","j"], "c"))
print(sol1.nextGreatestLetter2(["x","x","y","y"], "z"))