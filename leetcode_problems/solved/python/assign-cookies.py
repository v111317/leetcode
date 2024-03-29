#https://leetcode.com/problems/assign-cookies/description/

# Assume you are an awesome parent and want to give your children some cookies. 
# But, you should give each child at most one cookie.

# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; 
# and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, 
# and the child i will be content. Your goal is to maximize the number of your content children 
# and output the maximum number.

#revise
from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        if len(s)==0:
            return 0
        
        g.sort()
        s.sort()
        fulfilled = 0
        
        if g[0] > s[len(s)-1]:
            return 0
        j = 0
        i = 0
        while i < len(g):
            if s[j]>=g[i]:
                fulfilled += 1
                # j += 1
                i += 1
            j += 1    
            if j > len(s)-1:
                    break
        
        return fulfilled
    
    def findContentChildren2(self, g: List[int], s: List[int]) -> int:
        if len(s)==0:
            return 0
        
        g.sort()
        s.sort()
        
        j = 0
        fulfilled = 0
        for i in range(len(s)):
            if s[i]>=g[j]:
                fulfilled += 1
                j += 1
            if j > len(g)-1:
                break
        
        return fulfilled
        
        
sol1 = Solution()
print(sol1.findContentChildren([1,2,3], [1,1]))
print(sol1.findContentChildren([1,2], [1,2,3]))
                
#solution 1
#time - O(n)
#space - O(1)        

#solution 2
#time - O(n)
#space - O(1)        
