#https://leetcode.com/problems/positions-of-large-groups/description/

# In a string s of lowercase letters, these letters form consecutive groups of 
# the same character.

# For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", 
# and "yy".
# A group is identified by an interval [start, end], where start 
# and end denote the start and end indices (inclusive) of the group. 
# In the above example, "xxxx" has the interval [3,6].
# A group is considered large if it has 3 or more characters.
# Return the intervals of every large group sorted in increasing order by start index.

from typing import List

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        
        if len(s) < 3:
            return []
        
        result = []
        ch = s[0]
        count = 1
        group = [0, 0]
        for i in range(1, len(s)):
            
            if s[i]==ch:
                count += 1
                if i==len(s)-1 and count>=3:
                    group[1] = i
                    result.append(group)
            else:
                ch = s[i]
                if count>=3:
                    group[1] = i-1
                    result.append(group)
                    group = []
                count = 1
                group = [i, i]

        return result
    
sol1 = Solution()
print(sol1.largeGroupPositions("abcdddeeeeaabbbcd"))   
print(sol1.largeGroupPositions("abbxxxxzzy"))
print(sol1.largeGroupPositions("aaabbb")) 
print(sol1.largeGroupPositions("aaa"))            
 #time - O(n)
 #space - O(1)               
            