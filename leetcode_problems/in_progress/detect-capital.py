#https://leetcode.com/problems/detect-capital/description/

# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
      
        count = len(word)
      
        if count == 1:
          return True
      
        
        for letter in word:
            if ord(letter) >= 65 and ord(letter) <= 90:
                a = 1
            #97-122
        
        
#time
#space