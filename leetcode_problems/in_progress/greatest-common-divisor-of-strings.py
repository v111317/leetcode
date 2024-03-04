#https://leetcode.com/problems/greatest-common-divisor-of-strings/description/

# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t 
# (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        letterMap1 = {}
        letterMap2 = {}
        
        for s in str1:
            if s in letterMap1:
                letterMap1[s] += 1
            else:
                letterMap1[s] = 1
        
        for s in str2:
            if s in letterMap2:
                letterMap2[s] += 1
            else:
                letterMap2[s] = 1
        
        keys1 = list(letterMap1.keys())
        values1 = set(letterMap1.values())
        keys1.sort()
        
        keys2 = list(letterMap2.keys())
        values2 = set(letterMap2.values())
        keys2.sort()
        
        keyStr1 = "".join(keys1)
        keyStr2 = "".join(keys2)
        
        print(letterMap1)
        print(letterMap2)
        print(keyStr1, keyStr2)
        if keyStr1!=keyStr2:
            return ""

        if len(list(values1)) > 1 or len(list(values2)) > 1:
            return ""
        
        repeat1 = list(values1)[0]
        repeat2 = list(values2)[0]
        
        minRepeat = 1
        if repeat1 > repeat2:
            if repeat1%repeat2==0:
                minRepeat = repeat2
                return str2
            else:
                return str2[0:len(str2)//2]

        if repeat2 > repeat1:
            if repeat2%repeat1==0:
                minRepeat = repeat1
                return str1
            else:
                return str1[0:len(str1)//2]
            
sol1 = Solution()
# print(sol1.gcdOfStrings("ABCABC", "ABC"))
# print(sol1.gcdOfStrings("ABABAB", "ABAB"))
# print(sol1.gcdOfStrings("LEET", "CODE"))
print(sol1.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))
#"TAUXXTAUXXTAUXXTAUXXTAUXX"
#"TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"


            
