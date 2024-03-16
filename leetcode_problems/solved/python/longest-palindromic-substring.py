#https://leetcode.com/problems/longest-palindromic-substring/description/

#Given a string s, return the longest palindromic substring in s

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s)==1:
            return s
        
        iterableLen = len(s) * 2 - 2
        maxLen = 1
        maxPalin = ""
        for center in range(1, iterableLen):
            
            if center%2 == 0:
                count = 1
                rightIdx = center//2 + 1
                leftIdx = rightIdx - 2
            else:
                count = 0
                rightIdx = (center+1)//2
                leftIdx = rightIdx - 1
                
            while s[leftIdx]==s[rightIdx]:
                count += 2
                if count > maxLen:
                    maxLen = count
                    maxPalin = s[leftIdx:rightIdx+1]
                leftIdx -= 1
                if leftIdx < 0:
                    break
                rightIdx += 1
                if rightIdx > len(s)-1:
                    break
        if maxLen==1:
            return s[0]
        else:        
            return maxPalin
                    
        
sol1 = Solution()
print(sol1.longestPalindrome("babad"))    
print(sol1.longestPalindrome("cbbd"))  
print(sol1.longestPalindrome("ac"))
print(sol1.longestPalindrome("a"))     
print(sol1.longestPalindrome("ccc"))       

#time - O(n*n)
#space - O(1)