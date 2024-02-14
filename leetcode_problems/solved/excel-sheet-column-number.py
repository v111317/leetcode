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
print("L", sol1.titleToNumber("L"))
print("CVA", sol1.titleToNumber("CVA"))
print("A", sol1.titleToNumber("A"))
print("ZY", sol1.titleToNumber("ZY"))
print("ZA", sol1.titleToNumber("ZA"))
print("AZS", sol1.titleToNumber("AZS"))
print("YZ", sol1.titleToNumber("YZ"))
print("ZZY", sol1.titleToNumber("ZZY"))
# 12 L
# 2601 CVA
# 28 AB
# 1 A
# 701 ZY
# 677 ZA
# 1371 AZS
# 676 YZ
# 18277 ZZY

#time - O(n)
#space - O(1)