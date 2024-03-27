#https://leetcode.com/problems/teemo-attacking/

# Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned 
# for a exactly duration seconds. More formally, an attack at second t will mean Ashe is poisoned during the 
# inclusive time interval [t, t + duration - 1]. If Teemo attacks again before the poison effect ends, the timer 
# for it is reset, and the poison effect will end duration seconds after the new attack.

# You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo attacks 
# Ashe at second timeSeries[i], and an integer duration.

# Return the total number of seconds that Ashe is poisoned.
from typing import List

class Solution:
    #time limit exceeded
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        result = set()
        for t in timeSeries:
            for i in range(t, t+duration):
                result.add(i)
        return len(result)

    def findPoisonedDuration2(self, timeSeries: List[int], duration: int) -> int:
        result = 0
        for i in range(len(timeSeries)-1):
            if timeSeries[i+1] - timeSeries[i] > duration:
                result += duration
            else:
                result += timeSeries[i+1] - timeSeries[i]
                
        return result + duration

sol1 = Solution()
print(sol1.findPoisonedDuration2([1,4], 2))
print(sol1.findPoisonedDuration2([1,2], 2))
print(sol1.findPoisonedDuration2([1,2,3,4,5,6,7,8,9], 1))
