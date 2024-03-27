#https://leetcode.com/problems/richest-customer-wealth/description/

# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer 
# has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is
# the customer that has the maximum wealth.

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        totalAmount = 0
        maxAmount = 0
        for i in range(0, len(accounts)):
            # print(i)
            custAccounts = accounts[i]
            totalAmount = sum(custAccounts)
            if totalAmount > maxAmount:
                maxAmount = totalAmount
        return maxAmount
    
#time - O(no. of account)
#space - O(1)
