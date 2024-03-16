#https://leetcode.com/problems/relative-ranks/description/

# You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. 
# All the scores are guaranteed to be unique.

# The athletes are placed based on their scores, where the 1st place athlete has the highest score, 
# the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete, their rank is their placement number (i.e., 
# the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ith athlete.
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        playerScores = score.copy()
        
        playerScores.sort(reverse=True)
        scoreMap = {}
        
        for i, s in enumerate(playerScores):
            match i:
                case 0:
                    scoreMap[s] = "Gold Medal"
                case 1:
                    scoreMap[s] = "Silver Medal"
                case 2:
                    scoreMap[s] = "Bronze Medal"
                case _ :
                    scoreMap[s] = str(i+1)
        result = []
        for s in score:
            result.append(scoreMap[s])
        return result
    
sol1 = Solution()
print(sol1.findRelativeRanks([5,4,3,2,1]))
print(sol1.findRelativeRanks([10,3,8,9,4]))

#time - O(nlogn)
#space - O(n)