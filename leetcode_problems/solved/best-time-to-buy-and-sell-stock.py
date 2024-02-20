#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# You are given an array prices where prices[i] is the price of a given stock 
# on the ith day.

# You want to maximize your profit by choosing a single day to buy one 
# stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. 
# If you cannot achieve any profit, return 0.


from typing import List

class Solution:
    #Time Limit Exceeded
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        max = 0
        for i in range(0, len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    profit = prices[j] - prices[i]     
                    if profit > max:
                        max = profit
        return max
    
    def maxProfit2(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        
        for i in range(1, len(prices)):
            profit = prices[i] - minPrice
            maxProfit = max(profit, maxProfit)
            minPrice = min(prices[i], minPrice)
        
        return maxProfit
        
# sol1 = Solution()
# print(sol1.maxProfit2([7,1,5,3,6,4]))
# print(sol1.maxProfit2([7,6,4,3,1]))


#solution 1 
#time - O(n*n)
#space - O(1)

#solution 2
#time - O(n)
#space - O(1)

        