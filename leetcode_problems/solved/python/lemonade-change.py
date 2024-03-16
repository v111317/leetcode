#https://leetcode.com/problems/lemonade-change/description/

# At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to 
# buy from you and order one at a time (in the order specified by bills). 
# Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.
# You must provide the correct change to each customer so that the net transaction 
# is that the customer pays $5.

# Note that you do not have any change in hand at first.

# Given an integer array bills where bills[i] is the bill the ith customer pays, 
# return true if you can provide every customer with the correct change, 
# or false otherwise.
from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        depositMap = {5:0, 10:0, 20:0}
        total = 0
        i = 0
        for idx, bill in enumerate(bills):
            total = (idx+1)*5
            change = bill - 5
            
            if change == 0:
                depositMap[bill] += 1
                continue
            
            if change > total:
                return False
            
            match change:
                case 5:
                    if depositMap[5]<=0:
                        return False
                    else:
                        depositMap[5] -= 1
                case 10:
                    if depositMap[10]>0:
                        depositMap[10] -= 1
                    elif depositMap[5]>=2:
                        depositMap[5] -= 2
                    else:
                        return False
                case 15:
                    if depositMap[10]>=1 and depositMap[5]>=1:
                        depositMap[5] -=1 
                        depositMap[10] -= 1
                    elif depositMap[5]>=3:
                        depositMap[5] -= 3   
                    else:
                        return False
            depositMap[bill] += 1
        return True

sol1 = Solution()
print(sol1.lemonadeChange([5,5,5,10,20]))   
print(sol1.lemonadeChange([5,5,10,10,20]))   
     
        
#time - O(n)
#space - O(1)