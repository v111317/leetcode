#https://leetcode.com/problems/unique-morse-code-words/description/

# International Morse Code defines a standard encoding where each letter is mapped to a series of dots 
# and dashes, as follows:

# 'a' maps to ".-",
# 'b' maps to "-...",
# 'c' maps to "-.-.", and so on.
# For convenience, the full table for the 26 letters of the English alphabet is given below:

# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Given an array of strings words where each word can be written as a concatenation of the Morse code 
# of each letter.

# For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", 
# and "-...". We will call such a concatenation the transformation of a word.
# Return the number of different transformations among all words we have.
from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseCodeMap = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = set()
        for word in words:
            wordInMorse = ""
            for letter in word:
                wordInMorse += morseCodeMap[ord(letter)-97]
            
            #print(wordInMorse)
            result.add(wordInMorse)
        
        return len(result)

sol1 = Solution()
print(sol1.uniqueMorseRepresentations(["gin","zen","gig","msg"]))
