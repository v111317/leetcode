#https://leetcode.com/problems/shortest-completing-word/description/

# Given a string licensePlate and an array of strings words, find the shortest completing word in words.

# A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate,
# and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear 
# in the word the same number of times or more.

# For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. 
# Possible completing words are "abccdef", "caaacab", and "cbca".

# Return the shortest completing word in words. It is guaranteed an answer exists. 
# If there are multiple shortest completing words, return the first one that occurs in words.
from typing import List

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        letters = []
        for ch in licensePlate:
            if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
                letters.append(ch.lower())
        
        lettersLen = len(letters)
        shorestLen = float('inf')
        shortestWord = ""
        
        for word in words:
            lettersCopy = letters.copy()
            count = lettersLen
            for ch in word:
                if ch in lettersCopy:
                    count -= 1
                    lettersCopy.remove(ch)
            if count==0:
                if len(word) < shorestLen:
                    shortestWord = word
                    shorestLen = len(word)
        return shortestWord

sol1 = Solution()
print(sol1.shortestCompletingWord("1s3 PSt", ["step","steps","stripe","stepple"]))  
print(sol1.shortestCompletingWord("1s3 456", ["looks","pest","stew","show"]))  
