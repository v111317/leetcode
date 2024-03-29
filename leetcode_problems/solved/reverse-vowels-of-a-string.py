#https://leetcode.com/problems/reverse-vowels-of-a-string/description/

# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s)==1:
            return s
        
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        start = 0
        end = len(s)-1
        while start < end:
            if s[start] not in vowels:
                start += 1
                    
            if s[end] not in vowels:
                end -= 1
            
            if s[start] in vowels and s[end] in vowels:
                temp = s[start]
                s[start] = s[end]
                s[end] = temp
                start += 1
                end -= 1
            
        return "". join(s)
    
sol1 = Solution()
print(sol1.reverseVowels("hello"))
print(sol1.reverseVowels("leetcode"))
print(sol1.reverseVowels("aA"))

#time - O(n)
#space - O(1)
