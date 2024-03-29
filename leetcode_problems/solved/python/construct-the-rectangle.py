#https://leetcode.com/problems/construct-the-rectangle/description/

# A web developer needs to know how to design a web page's size. So, given a specific rectangular web page’s area, 
# your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:

# The area of the rectangular web page you designed must equal to the given target area.
# The width W should not be larger than the length L, which means L >= W.
# The difference between length L and width W should be as small as possible.
# Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.
from typing import List
import math

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        halfway = int(math.sqrt(area))
        minDiff = area
        result = []
        
        for i in range(halfway, 0, -1):
            if area%i==0:
                length = i
                breadth = area // i
                if abs(length-breadth) < minDiff:
                    minDiff = abs(length-breadth)
                    result = [length, breadth] 
        result.sort(reverse=True)
        return result
    
sol1 = Solution()
print(sol1.constructRectangle(4))
print(sol1.constructRectangle(37))
print(sol1.constructRectangle(122122))

#time - O(sqrt(n))
#space - O(1)