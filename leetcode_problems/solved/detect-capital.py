#https://leetcode.com/problems/detect-capital/description/

# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
    
        if len(word) == 1:
            return True
          
        isCapital = False
        isCheck = True  
        for i in range(1, len(word)):
            letter = word[i]
            if isCheck:
                if ord(letter) >= 65 and ord(letter) <= 90: #capital
                    isCapital = True
                else:
                    isCapital = False
                isCheck = False
                
            if isCapital:
                if ord(letter) >= 65 and ord(letter) <= 90:
                    continue
                else:
                    return False
            
            if not isCapital:
                if ord(letter) >= 97 and ord(letter) <= 122:
                    continue
                else:
                    return False
        
        if isCapital:
            if ord(word[0]) >= 65 and ord(word[0]) <= 90:    
                return True
            else:
                return False
        
        if not isCapital:
            return True
            
        
sol1 = Solution()
print(sol1.detectCapitalUse("USA"))
print(sol1.detectCapitalUse("leetcode"))
print(sol1.detectCapitalUse("Maple"))
print(sol1.detectCapitalUse("MaplA"))
print(sol1.detectCapitalUse("aaAla"))
        
#time - O(n)
#space - O(1)