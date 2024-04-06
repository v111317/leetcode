#https://leetcode.com/problems/di-string-match/description/

# A permutation perm of n + 1 integers of all the integers in the range [0, n] 
# can be represented as a string s of length n where:

# s[i] == 'I' if perm[i] < perm[i + 1], and
# s[i] == 'D' if perm[i] > perm[i + 1].
# Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, 
# return any of them.
from typing import List

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        i = 0
        j = len(s)
        
        result = []
        for letter in s:
            if letter == "I":
                result.append(i)
                i += 1
            else:
                result.append(j)
                j -= 1
        
        result.append(i)
        return result

sol1 = Solution()
print(sol1.diStringMatch("IDID"))
print(sol1.diStringMatch("III"))
print(sol1.diStringMatch("DDI"))
