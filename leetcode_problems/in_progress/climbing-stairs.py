class Solution:
    def climbStairs(self, n: int) -> int:
        print(n)
        
        if n in [1, 0]:
            return n
        
        countWithFirstStep1 = (1 + self.climbStairs(n-1)) if n-1 > 0 else 0 
        countWithFirstStep2 = (1 + self.climbStairs(n-2)) if n-2 > 0 else 0
        
        return countWithFirstStep1 + countWithFirstStep2
    
sol1 = Solution()
print(sol1.climbStairs(3))