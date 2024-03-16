#https://leetcode.com/problems/last-stone-weight/
# You are given an array of integers stones where stones[i] is 
# the weight of the ith stone.

# We are playing a game with the stones. On each turn, 
# we choose the heaviest two stones and smash them together. 
# Suppose the heaviest two stones have weights x and y with x <= y. 
# The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y 
# has new weight y - x. At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        countStones = len(stones)
        
        if countStones==1:
            return stones[0]
        
        countZero = 0
        i = countStones - 1
        while countZero!=countStones-1:
            stones.sort()
            print(stones)
            stones[i] = stones[i] - stones[i-1]
            stones[i-1] = 0
            countZero += 1
            print(stones)
            
        return stones[i]
    
sol1 = Solution()    
print(sol1.lastStoneWeight([2,7,4,1,8,1]))
#time - O(n*nlogn)
#space - O(1)