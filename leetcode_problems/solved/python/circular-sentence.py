#https://leetcode.com/problems/circular-sentence/description/

# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

# For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
# Words consist of only uppercase and lowercase English letters. 
# Uppercase and lowercase English letters are considered different.

# A sentence is circular if:

# The last character of a word is equal to the first character of the next word.
# The last character of the last word is equal to the first character of the first word.
# For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular sentences. 
# However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.

# Given a string sentence, return true if it is circular. Otherwise, return false.

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
        count = 0
        words = sentence.split(" ")
        
        if len(words)==1:
            word = words[0]
            if word[0] == word[len(word)-1]:
                return True
            else:
                return False
        
        for i, word in enumerate(words):
            if i==len(words)-1:
                if word[len(word)-1]==words[0][0]:
                    return True
                else:
                    return False
            if word[len(word)-1]==words[i+1][0]:
                count += 1
            else:
                return False

sol1 = Solution()
print(sol1.isCircularSentence("leetcode exercises sound delightful"))
print(sol1.isCircularSentence("Leetcode is cool"))

#time - O(n) - n = no. of words
#space - O(n) 
