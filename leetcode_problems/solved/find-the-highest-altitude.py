#https://leetcode.com/problems/find-the-highest-altitude/description/

# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. 
# The biker starts his trip on point 0 with altitude equal 0.

# You are given an integer array gain of length n where gain[i] is the net gain in altitude between 
# points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currAlt = 0
        maxAlt = 0
        for altitude in gain:
            currAlt += altitude
            maxAlt = max(maxAlt, currAlt)
            
        return maxAlt

sol1 = Solution()
# print(sol1.largestAltitude([-5,1,5,0,-7]))
print(sol1.largestAltitude([-4,-3,-2,-1,4,3,2]))
