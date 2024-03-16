#https://leetcode.com/problems/find-common-characters/description/

# Given a string array words, return an array of all characters that show up in all strings within the words 
# (including duplicates). You may return the answer in any order.
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        numWords = len(words)
        
        if numWords==1:
            return list(words[0])
        
        letterMap = {}
        
        for letter in words[0]:
            if letter in letterMap:
                letterMap[letter] += 1
            else:
                letterMap[letter] = 1
        
        for i in range(1, numWords):
            commonLetters = []
            for letter in words[i]:
                
                if letter in letterMap and letterMap[letter]>0:
                    letterMap[letter] -= 1
                    commonLetters.append(letter)
              
            letterMap = {}
            for letter in commonLetters:
                if letter in letterMap:
                    letterMap[letter] += 1
                else:
                    letterMap[letter] = 1
        result = ""
        for key, value in letterMap.items():
            result += key * value
        
        return list(result)

sol1 = Solution()
print(sol1.commonChars(["bella","label","roller"]))    
print(sol1.commonChars(["cool","lock","cook"]))    

# time - O(k*n) - k is no. of words
# space - O(m) - m is length of largest word