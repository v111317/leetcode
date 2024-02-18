from typing import List

class Solution:
    def maxProfit2(self, prices: List[int]) -> int:
        
        profit = 0
        max = 0
        for i in range(0, len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    profit = prices[j] - prices[i]     
                    if profit > max:
                        max = profit
        return max
    
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        max = 0
        pricesSorted = prices
        pricesSorted.sort()
        print(pricesSorted)
        
                        
        return max
    
sol1 = Solution()
print(sol1.maxProfit([7,1,5,3,6,4]))
print(sol1.maxProfit([7,6,4,3,1]))

        