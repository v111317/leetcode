#https://leetcode.com/problems/longest-palindrome/description/

# Given a string s which consists of lowercase or uppercase letters, return the length 
# of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        letterMap = {}
        for letter in s:
            if letter in letterMap:
                letterMap[letter] += 1
            else:
                letterMap[letter] = 1
        valuesList = list(letterMap.values())
        isOne = False
        count = 0
        for n in valuesList:
            if n%2==1:
                isOne =True
            count += int(n/2)
        
        count = count*2
        if isOne:
            count += 1
        return count

sol1 = Solution()
# print(sol1.longestPalindrome("abccccdd"))
# print(sol1.longestPalindrome("aabb"))
print(sol1.longestPalindrome("ccc"))
#print(sol1.longestPalindrome("ababababa"))

#time- O(n)
#space - O(n)
                