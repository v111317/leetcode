#https://leetcode.com/problems/insert-interval/description/

# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
# represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
# You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and 
# intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Note that you don't need to modify intervals in-place. You can make a new array and return it.
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start = newInterval[0]
        end = newInterval[1]
        
        
        
        result = []
        #add edge cases
        if len(intervals)>0:
            if end < intervals[0][0]:
                result.append([start, end])
                result = result + intervals
                return result
            elif start > intervals[len(intervals)-1][1]:
                result = intervals
                result.append([start, end])
                return result
        
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        for interval in intervals:
            #print(start, end, interval)
            if start>=interval[0] and start<=interval[1]:
                newStart = min(interval[0], start)
                newEnd = max(interval[1], end)
            
                start = newStart
                end = newEnd
                
            elif start <= interval[0] and end >= interval[0]:
                newStart = min(interval[0], start)
                newEnd = max(interval[1], end)
                start = newStart
                end = newEnd
            else:
                if start>interval[1]:
                    result.append(interval)
                else:
                    result.append([start, end])
                    start = interval[0]
                    end = interval[1]
                
        result.append([start,end])       
        return result
    
sol1 = Solution()
print(sol1.insert([[1,3],[6,9]], [2,5]))
print(sol1.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
