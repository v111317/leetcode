#https://leetcode.com/problems/can-place-flowers/description/

# You have a long flowerbed in which some of the plots are planted, and some are not. 
# However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty 
# and 1 means not empty, and an integer n, return true if n new flowers can be planted 
# in the flowerbed without violating the no-adjacent-flowers rule 
# and false otherwise.
from typing import List
import math

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed):
            if flowerbed[i]==1:
                if i>=1:
                    flowerbed[i-1] = 2
                if i < len(flowerbed)-1:
                    flowerbed[i+1] = 2
                i += 2
            else:
                i += 1
        flowerCount = 0
        zeroCount = 0
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                zeroCount += 1
            else:
                flowerCount += math.ceil(zeroCount/2)
                zeroCount = 0
        if zeroCount>0:
            flowerCount += math.ceil(zeroCount/2)
        return flowerCount >= n

sol1 = Solution()
print(sol1.canPlaceFlowers([1,0,0,0,1], 1))
print(sol1.canPlaceFlowers([1,0,0,0,1], 2))
print(sol1.canPlaceFlowers([1,0,0,0,1,0,0], 2))
print(sol1.canPlaceFlowers([1,0,1,0,0,1,0], 1))


        
#time - 
#space - 