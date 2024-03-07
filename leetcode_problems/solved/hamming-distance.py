#https://leetcode.com/problems/hamming-distance/description/

# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, return the Hamming distance between them.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xBin = bin(x)
        yBin = bin(y)
        xBin = xBin[2:]
        yBin = yBin[2:]
        diffLen = abs(len(xBin) - len(yBin))
        if len(xBin)>len(yBin):
            yBin = "0" * diffLen + yBin
        else:
            xBin = "0" * diffLen + xBin
        
        count = 0 
        for i, ch in enumerate(xBin):
            if ch != yBin[i]:
                count += 1
        return count
        
        
sol1 = Solution()
print(sol1.hammingDistance(4,1))
print(sol1.hammingDistance(3,1))

#time - O(n)
#space - O(n)