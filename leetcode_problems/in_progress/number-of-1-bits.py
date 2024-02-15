class Solution:
    def hammingWeight(self, n: int) -> int:
        intStr = bin(n)
        
        intStr = intStr[2:]
        
        countOnes = 0
        for bit in intStr:
            if int(bit):
                countOnes += 1
                
        return countOnes
    

sol1 = Solution()
#print(sol1.hammingWeight(11111111111111111111111111111101))
print(sol1.hammingWeight(1343434343))

                