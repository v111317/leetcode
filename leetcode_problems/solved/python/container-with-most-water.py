#https://leetcode.com/problems/container-with-most-water/description/

# You are given an integer array height of length n. There are n vertical lines drawn such that the 
# two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.
from typing import List

class Solution:
    #time limit exceeded
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        vol = 0
        maxVol = float('-inf')
        for i in range(n):
            for j in range(i+1, n):
                vol = min(height[i], height[j]) * (j-i)
                maxVol = max(maxVol, vol)
                # print(i, j, vol)
    
        return maxVol
    
    def maxArea2(self, height: List[int]) -> int:
        n = len(height)
        vol = 0
        maxVol = float('-inf')
        
        start = 0
        end = n - 1
        
        while start < end:
            vol = (min(height[end], height[start])) * (end-start)
            maxVol = max(maxVol, vol)
            
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
    
        return maxVol
    
sol1 = Solution()
print(sol1.maxArea2([1,8,6,2,5,4,8,3,7]))

