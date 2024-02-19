#https://leetcode.com/problems/reverse-bits/description/

#Reverse bits of a given 32 bits unsigned integer.

class Solution:
    def reverseBits(self, n: int) -> int:
        num = str(n)
        revNum = num[::-1]
        return int(revNum, 2)
    
sol1 = Solution()
#print(sol1.reverseBits(int(00000010100101000001111010011100)))