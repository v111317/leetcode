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
            if len(result)==0: 
                result.append(asteroid)
                continue
            
            collResult = -1
            while len(result)>0 and collResult<0:
                
                n = len(result)
                top = result[n-1]
                if top > 0:               
                    if asteroid > 0: 
                        result.append(asteroid)
                        break
                    else:
                        if abs(asteroid)>=top:
                            result.pop()
                            if len(result)==0 and abs(asteroid)>top:
                                result.append(asteroid)
                                collResult = -1
                            else:
                                collResult = 1 #fix here
                        else:
                            collResult = 1
                else:
                    result.append(asteroid)
                    break
                print(asteroid, result, collResult)
        return result
    
sol1 = Solution()
# print(sol1.asteroidCollision([5, 10, -5]))  
# print(sol1.asteroidCollision([8, -8]))
# print(sol1.asteroidCollision([10, 2, -5]))
# print(sol1.asteroidCollision([-2,-1,1,2]))
# print(sol1.asteroidCollision([-2,-2,1,-1]))
print(sol1.asteroidCollision([-2,-2,1,-2]))

                    
                            
                
            
            
            
            
            
