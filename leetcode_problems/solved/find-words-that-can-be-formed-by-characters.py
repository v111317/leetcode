#https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

# You are given an array of strings words and a string chars.

# A string is good if it can be formed by characters from chars 
# (each character can only be used once).

# Return the sum of lengths of all good strings in words.

from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        letterMap = {}
        for l in chars:
            if l in letterMap:
                letterMap[l] += 1
            else:
                letterMap[l] = 1
                
        letterMapOrg = letterMap.copy()
        isMatch = True
        goodStr = []
        
        for word in words:
            count = 0
            letterMap = letterMapOrg.copy()
            for w in word:
                if w in letterMap and letterMap[w]>0:
                    letterMap[w] -= 1
                    count += 1
                else:
                    break
            if count==len(word):
                goodStr.append(word)
        
        result = 0        
        for word in goodStr:
            result += len(word)
        return result
            
sol1 = Solution()
print(sol1.countCharacters(["cat","bt","hat","tree"], "atach"))
print(sol1.countCharacters(["hello","world","leetcode"], "welldonehoneyr"))

#time - O(n*n)
#space - O(n)