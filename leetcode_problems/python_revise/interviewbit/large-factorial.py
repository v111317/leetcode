# https://www.interviewbit.com/problems/large-factorial/

# Given a number A. Find the fatorial of the number.

class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):
        result = 1
        for i in range(2, A+1):
            result *= i
        return result   
    
sol1 = Solution()
print(sol1.solve(10))
print(sol1.solve(100))