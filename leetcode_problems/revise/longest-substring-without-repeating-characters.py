#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

#Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sLen = len(s)
        if sLen <= 1:
            return sLen
        startIdx = 0
        endIdx = 0
        maxLen = 1
        letterMap = {s[0]:1}
        i = 1
        while i < sLen:
            if s[i] not in letterMap:
                letterMap[s[i]] = 1
                endIdx += 1
                if i == sLen-1:
                    maxLen = max(maxLen, endIdx-startIdx+1)
            else:
                maxLen = max(maxLen, endIdx-startIdx+1)
                startIdx += 1
                endIdx = startIdx
                i = startIdx
                letterMap = {s[startIdx]:1}
            i += 1    
        return maxLen

    #start from the last matched character instead of moving the startIdx by 1
    def lengthOfLongestSubstring2(self, s: str) -> int:
        a = 1
        #https://leetcode.com/problems/longest-substring-without-repeating-characters/solutions/3649636/3-method-s-c-java-python-beginner-friendly/
    
sol1 = Solution()
print(sol1.lengthOfLongestSubstring("abcabcbb"))  
print(sol1.lengthOfLongestSubstring("bbbbb"))         
print(sol1.lengthOfLongestSubstring("pwwkew"))         

#time - O(n*n)
#space - O(1)