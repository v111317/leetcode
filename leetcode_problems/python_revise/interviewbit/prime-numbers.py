#https://www.interviewbit.com/problems/prime-numbers/

#Given a number A, find all prime numbers up to A (A included).
#Make sure the returned array is sorted.
import math

class Solution:
    
    def isPrime(self, num):
        sqrtNum = int(math.sqrt(num))
        for i in range(2, sqrtNum+1):
            if num%i==0:
                return False
        return True
    
	# @param A : integer
	# @return a list of integers
    def sieve(self, A):
        result = []
        for i in range(2, A+1):
            if(self.isPrime(i)):
                result.append(i)
        
        return result

sol1 = Solution()
print(sol1.sieve(17))
    
