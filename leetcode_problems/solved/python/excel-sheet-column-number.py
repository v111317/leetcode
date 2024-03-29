#https://leetcode.com/problems/excel-sheet-column-number/description/

#Given a string columnTitle that represents the column title as appears 
# in an Excel sheet, return its corresponding column number.

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        letterMap = {
            'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 
            'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 
            'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 
            'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 
            'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 
            'Z': 26
        }
        
        colNum = 0
        j = 0
        for i in range(len(columnTitle)-1, -1, -1):
            colNum += letterMap[columnTitle[i]] * pow(26, j)
            j += 1
        
        return colNum
    
        
sol1 = Solution()
print("AB", sol1.titleToNumber("AB"))
# print("L", sol1.titleToNumber("L"))
# print("ZA", sol1.titleToNumber("ZA"))
# print("AZS", sol1.titleToNumber("AZS"))

# 12 L
# 677 ZA
# 1371 AZS

#time - O(n)
#space - O(1)