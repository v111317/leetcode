class Solution:
	# @param A : integer
	# @return a strings
    def findDigitsInBinary(self, A):
        binNum = bin(A)
        print(binNum)
        return binNum[2:]
    
sol1 = Solution()
print(sol1.findDigitsInBinary(1))