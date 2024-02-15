class Solution:
    
    stepsMap = {}
    
    def climbStairs(self, n: int) -> int:
        
        if n in [0, 1]:
            return 1
        
        if n >= 2:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
        else:
            return self.climbStairs(n-1)
    
sol1 = Solution()
print(sol1.climbStairs(5))
print(sol1.climbStairs(44))

#time - O()
#space - O(1)
#tle