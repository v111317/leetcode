#https://leetcode.com/problems/maximum-number-of-balloons/description/

# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        goalStr = ['b', 'a', 'l', 'o', 'n']
        
        letterMap = {}
        for n in text:
            if n in letterMap:
                letterMap[n] += 1
            else:
                letterMap[n] = 1
        
        minNum = 10001
        
        for letter in goalStr:
            if letter in letterMap:
                if letter in ['b','a','n']:
                    minNum = min(minNum, letterMap[letter])
                else:
                    minNum = min(minNum, letterMap[letter]//2)
            else:
                return 0
        
        return minNum
    
sol1 = Solution()
print(sol1.maxNumberOfBalloons("nlaebolko"))
print(sol1.maxNumberOfBalloons("loonbalxballpoon"))  
print(sol1.maxNumberOfBalloons("leetcode"))  
        
        
#time - O(n)
#space - O(1)