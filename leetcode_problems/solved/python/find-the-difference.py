#https://leetcode.com/problems/find-the-difference/description/

# You are given two strings s and t.
# String t is generated by random shuffling string s and then add one more letter at a random position.
# Return the letter that was added to t.

#revise
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        if len(s)==0:
            return t
        
        letterMap = {}
        for letter in t:
            if letter in letterMap:
                letterMap[letter] += 1
            else:
                letterMap[letter] = 1
        
        for letter in s:
            if letter in letterMap:
                letterMap[letter] -= 1

        for key, value in letterMap.items():
            if value==1:
                return key
            
    def findTheDifference2(self, s: str, t: str) -> str:
        a = 1
        #implement using xor
            
sol1 = Solution()
print(sol1.findTheDifference("abcd", "abcde"))
print(sol1.findTheDifference("", "a"))
print(sol1.findTheDifference("a", "aa"))

#time - O(n)
#space - O(n)