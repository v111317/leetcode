#https://leetcode.com/problems/verifying-an-alien-dictionary/description/

# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order.
# The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only 
# if the given words are sorted lexicographically in this alien language.
from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words)==1:
            return True
        
        n = len(words)
        
        i = 0
        while i < n-1:
            word = words[i]
            nextWord = words[i+1]
            
            start = 0
            while start < len(word) and start < len(nextWord):
                wordChar = word[start]
                nextWordChar = nextWord[start]
                if order.index(wordChar) < order.index(nextWordChar):
                    break
                elif order.index(wordChar) == order.index(nextWordChar):
                    start += 1
                    if start==len(nextWord) and len(word)>len(nextWord):
                        return False
                    continue
                else:
                    return False
            i += 1
            
        return True
    
sol1 = Solution()
# print(sol1.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
# print(sol1.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))
print(sol1.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))
print(sol1.isAlienSorted(["apap","app"], "abcdefghijklmnopqrstuvwxyz"))




