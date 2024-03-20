from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a = 1
        
        maxProfit = 0
        minPrice = prices[0]
        
        for i in range(1, len(prices)):
            profit = prices[i] - minPrice
            if profit > maxProfit:
                maxProfit = profit
            
            if prices[i] < minPrice:
                minPrice = prices[i]
        
        return maxProfit
        
sol1 = Solution()
print(sol1.maxProfit([7,1,5,3,6,4]))    
print(sol1.maxProfit([7,6,4,3,1]))    

            
        