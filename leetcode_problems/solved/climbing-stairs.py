#https://leetcode.com/problems/climbing-stairs/description/

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    
    stepMap = {}
    
    def climbStairs(self, n: int) -> int:
        
        
        print(n)
        if n in [0,1]:
            return 1
        
        if n ==2:
            return 2
        
        if n in self.stepMap:
            return self.stepMap[n]
        
        self.stepMap[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.stepMap[n]
        
    
sol1 = Solution()
#print(sol1.climbStairs(5))
print(sol1.climbStairs(10))

#time - O()
#space - O(1)
#tle