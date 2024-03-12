#https://leetcode.com/problems/number-complement/description/

# The complement of an integer is the integer you get when you flip all the 0's to 1's and 
# all the 1's to 0's in its binary representation.

# For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
# Given an integer num, return its complement.

class Solution:
    def findComplement(self, num: int) -> int:
        binNum = bin(num)
        binNum = binNum[2:]
        
        newNum = []
        for i in range(len(binNum)):
            if binNum[i]=="0":
                newNum.append("1")
            else:
                newNum.append("0")
                
        newNum = "".join(newNum)
        return int(newNum, 2)

sol1  = Solution()
print(sol1.findComplement(5))
print(sol1.findComplement(1))