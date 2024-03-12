#https://www.interviewbit.com/problems/verify-prime/

# Given a number N, verify if N is prime or not.

# Return 1 if N is prime, else return 0.
import math

class Solution:
	# @param A : integer
	# @return an integer
    def isPrime(self, A):
        sqrtNum = int(math.sqrt(A))
        
        for i in range(2, sqrtNum+1):
            if A%i==0:
                return 0
        return 1

sol1 = Solution()
print(sol1.isPrime(17))
print(sol1.isPrime(6))