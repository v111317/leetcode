from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        
        str1 = strs[0]
        
        commonStr = ""
        commonLetter = ""
        for idx, letter in enumerate(str1):
            
            for s in strs[1:len(strs)+1]:
            
                try:
                    #if s.index(letter) == idx:
                    if idx in [searchIdx for searchIdx, l in enumerate(s) if l==letter]:
                        commonLetter += letter
                    else:
                        return commonStr
                except:
                    return commonStr
        
            if len(commonLetter) == len(strs)-1:
                commonStr += commonLetter[0]
                commonLetter = ""
            else:
                return commonStr
            
        return commonStr   
    
    #zip the list
    def longestCommonPrefix2(self, strs: List[str]) -> str: 
        a = 1
    
sol1 = Solution()
#print(sol1.longestCommonPrefix(["flower","flow","flight"]))
#print(sol1.longestCommonPrefix(["dog","racecar","car"]))
#print(sol1.longestCommonPrefix(["a"]))
print(sol1.longestCommonPrefix(["aa", "aa"]))