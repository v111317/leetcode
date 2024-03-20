#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. 
# You can only hold at most one share of the stock at any time. However, you can buy it then immediately 
# sell it on the same day.

# Find and return the maximum profit you can achieve.
from typing import List

class Solution:
    
    # def maxProfitBetweenDays(self, prices, start, end, profitList):
    #     print(start, end, profitList)
    #     key = str(start) + "_" + str(end)
    #     if key in profitList:
    #         return profitList[key]
        
    #     if abs(end-start)<=1:
    #         partProfit = prices[end] - prices[start]
    #         print(" => pp ", partProfit)
            
    #         if partProfit > 0:
    #             profitList[key] = partProfit    
    #             return partProfit
    #         else:
    #             profitList[key] = 0
    #             return 0
        
    #     idx = -1
    #     while idx==-1:
    #         for i in range(start+1, end+1):
    #             if prices[i] > prices[start]:
    #                 idx = i
    #                 break
    #         if idx==-1:
    #             start += 1
    #     print(" => ", idx)
        
    #     profit = self.maxProfitBetweenDays(prices, start, idx, profitList) + self.maxProfitBetweenDays(prices, idx+1, end, profitList)
    #     profitList[key] = profit
    #     print(" => ", profitList)
        
    #     return profit
    
            
    
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyPrice= prices[0]
        i = 1
        while i < len(prices):
            if prices[i] > buyPrice:
                maxProfit += prices[i] - buyPrice
            buyPrice = prices[i]
            i += 1
        return maxProfit
                

sol1 = Solution()
print(sol1.maxProfit([7,1,5,3,6,4]))
print(sol1.maxProfit([1,2,3,4,5]))
        
        
                
