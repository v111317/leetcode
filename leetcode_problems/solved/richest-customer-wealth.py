from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        totalAmount = 0
        maxAmount = 0
        for i in range(0, len(accounts)):
            print(i)
            custAccounts = accounts[i]
            totalAmount = sum(custAccounts)
            if totalAmount > maxAmount:
                maxAmount = totalAmount
        return maxAmount
