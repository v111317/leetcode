#https://leetcode.com/problems/merge-intervals/description/

# Given an array of intervals where intervals[i] = [starti, endi], 
# merge all overlapping intervals, and return an array of the non-overlapping intervals that 
# cover all the intervals in the input.

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals, key=lambda x: x[0])
        minRange = intervals[0][0]
        maxRange = intervals[0][1]
        
        result = []
        for interval in intervals:
            if interval[0]>= minRange and interval[0]<=maxRange:
                maxRange = max(maxRange, interval[1])
                minRange = min(minRange, interval[0])
            else:
                result.append([minRange, maxRange])
                minRange =  float('+inf')
                maxRange = float('-inf')
                
        return result
        
        
sol1 = Solution()
print(sol1.merge([[1,3],[2,6],[8,10],[15,18]]))
        