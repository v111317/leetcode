#https://leetcode.com/problems/arranging-coins/description/

# You have n coins and you want to build a staircase with these coins. 
# The staircase consists of k rows where the ith row has exactly i coins. 
# The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.


import math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        steps = (-1 + math.sqrt(1+8*n))/2
        return int(steps)

sol1 = Solution()
print(sol1.arrangeCoins(5))
print(sol1.arrangeCoins(8))
print(sol1.arrangeCoins(55))

#time - O(1)
#space - O(1)