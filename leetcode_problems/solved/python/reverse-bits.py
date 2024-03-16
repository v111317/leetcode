#https://leetcode.com/problems/reverse-bits/description/

#Reverse bits of a given 32 bits unsigned integer.

class Solution:
    def reverseBits(self, n: int) -> int:
        binNum = bin(n)
        binNum = binNum[2::]
        binNum = "0"*(32-len(binNum)) + binNum
        newNum = binNum[::-1]
        return int(newNum, 2)
    
sol1 = Solution()
print(sol1.reverseBits(8))
print(sol1.reverseBits(964176192))
print(sol1.reverseBits(4294967293))

#print(sol1.reverseBits(int(00000010100101000001111010011100)))