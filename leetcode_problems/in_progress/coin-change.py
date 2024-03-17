#https://leetcode.com/problems/coin-change/description/

# You are given an integer array coins representing coins of different denominations 
# and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        count = 0
        i = len(coins)-3
        coins.sort()
        while amount!=0:
            # print(amount, coins[i])
            if amount >= coins[i]:
                count += amount // coins[i]
                amount %= coins[i]
                i -= 1
            else:
                if i<=0 and amount!=0:
                    return -1
                if i>0:
                    i -= 1    
        return count
    
sol1 = Solution()
# print(sol1.coinChange([1,2,5], 11))
# print(sol1.coinChange([2], 3))
# print(sol1.coinChange([1], 0))
# print(sol1.coinChange([2,5,10,1], 27))
print(sol1.coinChange([186,419,83,408], 6249))

            