#https://leetcode.com/problems/asteroid-collision/description/

# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign represents its direction 
# (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. 
# If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        result = []
        for asteroid in asteroids:
            if asteroid > 0:
                result.append(asteroid)
            else:
                collResult = asteroid
                if len(result) > 0:
                    while len(result)> 0 and collResult<0:
                        n = len(result)
                        top = result[n-1]
                        if top > 0:               
                            if abs(asteroid) > top:
                                result.pop()
                                collResult = asteroid
                            else:
                                result.append(top)
                                collResult = 0
                        else:
                            result.append(top)
                            collResult = 0
                        
                else:
                    result.append(asteroid)
                            
                
            
            
            
            
            
