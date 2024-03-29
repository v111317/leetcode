#https://leetcode.com/problems/zigzag-conversion/description/

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
#     (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s)==1 or numRows==1:
            return s
            
        
        result = [[] for i in range(numRows)]
        
        rowIdx = -1    
        isIncrement = True
        for letter in s:
            if isIncrement:
                rowIdx += 1
            else:
                rowIdx -= 1
                
            if rowIdx == numRows:
                isIncrement = False
                rowIdx -= 2                
            elif rowIdx == -1:
                isIncrement = True
                rowIdx += 2
                
            result[rowIdx].append(letter)
        
        resultStr = ""
        for row in result:
            resultStr += "".join(row) 
        
        return resultStr   
        
    
sol1 = Solution()
# print(sol1.convert("PAYPALISHIRING", 4))
print(sol1.convert("ABC", 1))
        
        