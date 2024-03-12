#https://www.interviewbit.com/problems/prettyprint/

#Print concentric rectangular pattern in a 2d matrix. 

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        n = A*2 - 1
        