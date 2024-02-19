#https://leetcode.com/problems/excel-sheet-column-title/description/

#Given an integer columnNumber, return its corresponding column title 
# as it appears in an Excel sheet.

import string
import math

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        letterMap = {0: 'Z', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 
                     11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 
                     21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}
        colName = ""
        
        while columnNumber!=0:
        
            quotient = math.floor(columnNumber / 26)
            remainder = columnNumber % 26
            if remainder==0:
                quotient -= 1
            columnNumber = quotient
            colName = letterMap[remainder] + colName 
            
        return colName
        
sol1 = Solution()
print(12, sol1.convertToTitle(12))
print(2601, sol1.convertToTitle(2601))
print(28, sol1.convertToTitle(28))
print(1, sol1.convertToTitle(1))
print(701, sol1.convertToTitle(701))
print(677, sol1.convertToTitle(677))
print(1371, sol1.convertToTitle(1371))
print(676, sol1.convertToTitle(676))
print(18277, sol1.convertToTitle(18277))

#time - O(log of n to base 26)
#space = O(1)