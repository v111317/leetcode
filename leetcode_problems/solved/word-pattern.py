#https://leetcode.com/problems/word-pattern/description/

# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern 
# and a non-empty word in s.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        patternMap = {}
        
        if len(pattern) != len(s):
            return False
        
        for idx, letter in enumerate(pattern):
            if letter in patternMap:
                if patternMap[letter]==s[idx]:
                    continue
                else:
                    return False
            else:
                if s[idx] in patternMap.values():
                    return False
                else:
                    patternMap[letter] = s[idx]
                
        return True
    
sol1 = Solution()
print(sol1.wordPattern("abba", "dog cat cat dog"))
print(sol1.wordPattern("abba", "dog cat cat fish"))
print(sol1.wordPattern("aaaa", "dog cat cat dog"))
print(sol1.wordPattern("aa", "dog"))
print(sol1.wordPattern("a", "dog"))
print(sol1.wordPattern("ab", "dog dog"))

#time - O(n) - n=no. of words
#space - O(n)