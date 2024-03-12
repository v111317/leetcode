class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return (A+B)%pow(10,7)
    
sol1 = Solution()
print(sol1.solve(2,3))