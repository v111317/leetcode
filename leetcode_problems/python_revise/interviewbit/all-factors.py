#https://www.interviewbit.com/problems/all-factors/

#Given a number A, find all factors of A.
import math

class Solution:
	# @param A : integer
	# @return a list of integers
    def allFactors(self, A):
        sqrtNum = int(math.sqrt(A))
        result = []
        for i in range(1, sqrtNum+1):
            if A%i==0:
                result.append(i)
                result.append(A//i)
        
        result = set(result)
        result = list(result)
        result.sort()
        return result
    
sol1 = Solution()
print(sol1.allFactors(6))   

        