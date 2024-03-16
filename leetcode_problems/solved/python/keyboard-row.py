#https://leetcode.com/problems/keyboard-row/description/

# Given an array of strings words, return the words that can be typed using 
# letters of the alphabet on only one row of American keyboard like the image below.

# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        letterMap = {}
        wordMap = {}
        for idx, word in enumerate(keyboard):
            
            for letter in word:
                if letter not in letterMap:
                    letterMap[letter] = idx
        result = []
        listNum = 0
        for word in words:
            if word.lower() not in wordMap:
                wordMap[word.lower()] = word
        isMatch = False
        for word in words:
            word = word.lower()
            listNum = letterMap[word[0]]
            for i in range(len(word)):
                if letterMap[word[i]]==listNum:
                    isMatch = True
                    continue
                else:
                    isMatch = False
                    break
            if isMatch and i==len(word)-1:
                result.append(word)
                
        for idx, word in enumerate(result):
            result[idx] = wordMap[word]
            
        return result
                
sol1 = Solution()
print(sol1.findWords(["Hello","Alaska","Dad","Peace"]))
print(sol1.findWords(["abdfs","cccd","a","qwwewm"]))

#time - O(k*n) - k = number of words
#space - O(k*n)                
                
