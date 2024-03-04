#https://leetcode.com/problems/greatest-common-divisor-of-strings/description/

# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t 
# (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if str1+str2!=str2+str1:
            return ""
        
        lenStr = math.gcd(len(str1), len(str2))
        return str1[0:lenStr]
        
            
sol1 = Solution()
print(sol1.gcdOfStrings("ABCABC", "ABC"))
print(sol1.gcdOfStrings("ABABAB", "ABAB"))
print(sol1.gcdOfStrings("LEET", "CODE"))
print(sol1.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))
#"TAUXXTAUXXTAUXXTAUXXTAUXX"
#"TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"


            
