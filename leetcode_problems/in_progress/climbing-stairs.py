class Solution:
    
    global stepsMap
    stepsMap = {}
    
    def climbStairs(self, n: int) -> int:
        
        print(n)
        if n <= 2:
            return n
        
        if n in stepsMap:
            return stepsMap[n]
        print(n-1, n-2)
        stepsMap[n] =  self.climbStairs(n-1) + self.climbStairs(n-2)
        
    
sol1 = Solution()
print(sol1.climbStairs(5))
print(sol1.climbStairs(44))

#time - O()
#space - O(1)
#tle