class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        binNum = bin(n)
        binNum = binNum[2::]
        
        if binNum[0]=="1" and binNum.count("0")==len(binNum)-1:
            return True
        else:
            return False
    
sol1 = Solution()
print(sol1.isPowerOfTwo(2))
print(sol1.isPowerOfTwo(6))
print(sol1.isPowerOfTwo(16))
        