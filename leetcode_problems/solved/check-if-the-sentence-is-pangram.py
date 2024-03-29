#https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/

# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, 
# return true if sentence is a pangram, or false otherwise.

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letterMap = {}
        for letter in sentence:
            if letter not in letterMap:
                letterMap[letter] = 1
                
        if len(letterMap.keys())==26:        
            return True
        else:
            return False

sol1 = Solution()
print(sol1.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print(sol1.checkIfPangram("leetcode"))