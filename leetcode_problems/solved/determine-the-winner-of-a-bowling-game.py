#https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/description/

# You are given two 0-indexed integer arrays player1 and player2, that represent the number of pins that 
# player 1 and player 2 hit in a bowling game, respectively.

# The bowling game consists of n turns, and the number of pins in each turn is exactly 10.

# Assume a player hit xi pins in the ith turn. The value of the ith turn for the player is:

# 2xi if the player hit 10 pins in any of the previous two turns.
# Otherwise, It is xi.
# The score of the player is the sum of the values of their n turns.

# Return
# 1 if the score of player 1 is more than the score of player 2,
# 2 if the score of player 2 is more than the score of player 1, and
# 0 in case of a draw
from typing import List

class Solution:
    
    def calculateScore(self, scores):
        
        totalScore = 0
        multiplyFactor = 1
        for i, score in enumerate(scores):
            
            if (i>=1 and scores[i-1]==10) or (i>=2 and scores[i-2]==10):
                multiplyFactor = 2
            else:
                multiplyFactor = 1
            
            totalScore += score * multiplyFactor
            
        return totalScore
    
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        player1Score = self.calculateScore(player1)
        player2Score = self.calculateScore(player2)
        
        if player1Score > player2Score:
            return 1
        elif player1Score < player2Score:
            return 2
        else:
            return 0
        
sol1 = Solution()
print(sol1.isWinner([4,10,7,9], [6,5,2,3]))
print(sol1.isWinner([3,5,7,6], [8,10,10,2]))
print(sol1.isWinner([2,3], [4,1]))
print(sol1.isWinner([7,7,4,7,7],[7,2,3,10,10]))

#time - O(n)
#space - O(1)