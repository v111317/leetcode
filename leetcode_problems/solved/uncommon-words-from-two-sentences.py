#https://leetcode.com/problems/uncommon-words-from-two-sentences/description/

# A sentence is a string of single-space separated words where each word consists only
# of lowercase letters.

# A word is uncommon if it appears exactly once in one of the sentences, 
# and does not appear in the other sentence.

# Given two sentences s1 and s2, return a list of all the uncommon words. 
# You may return the answer in any order.

from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        wordMap = {}
        s1 = s1.split(" ")
        for word in s1:
            if word not in wordMap:
                wordMap[word] = 1
            else:
                wordMap[word] += 1
                
        s2 = s2.split(" ")
        for word in s2:
            if word not in wordMap:
                wordMap[word] = 1
            else:
                wordMap[word] += 1
            
        keys = list(wordMap.keys())
        uncommonWords = []
        for key in keys:
            if wordMap[key] == 1:
                uncommonWords.append(key)
        
        return uncommonWords
    
    
sol1 = Solution()
print(sol1.uncommonFromSentences("this apple is sweet", "this apple is sour"))
print(sol1.uncommonFromSentences("apple apple", "banana"))    

#time - O(n) - n = words in sentence
#space - O(n)