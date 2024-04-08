#https://leetcode.com/problems/n-th-tribonacci-number/description/

# The Tribonacci sequence Tn is defined as follows: 

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.

class Solution:
    
    def findNthTerm(self, n, dp):
        if n in dp:
            return dp[n]
        
        if n <=2: 
            return dp[n]
        
        n1Term = 0
        if n-1 in dp:
            n1Term = dp[n-1]
        else:
            n1Term = self.findNthTerm(n-1, dp)
            dp[n-1] = n1Term
        
        n2Term = 0
        if n-2 in dp:
            n2Term = dp[n-2]
        else:
            n2Term = self.findNthTerm(n-2, dp)
            dp[n-2] = n2Term
        
        n3Term = 0
        if n-3 in dp:
            n3Term = dp[n-3]
        else:
            n3Term = self.findNthTerm(n-3, dp)
            dp[n-3] = n3Term
    
        return n1Term + n2Term + n3Term
    

    def tribonacci(self, n: int) -> int:
        dp = {0:0, 1:1, 2:1}
        return self.findNthTerm(n, dp)
    
sol1 = Solution()
print(sol1.tribonacci(6))
        