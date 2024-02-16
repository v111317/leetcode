class Solution:
    def isUgly(self, n: int) -> bool:
        
        if n==0:
            return False
        
        if n == 1:
            return True
        
        factors = [2, 3, 5]
        isFactor = False
        while n!=1:
            for factor in factors:
                if n%factor==0:
                    n /= factor
                    isFactor = True
                    break
                else:
                    isFactor = False
            if not isFactor:
                return False
        
        return True
    
sol1 = Solution()
print(sol1.isUgly(0))
print(sol1.isUgly(6))
print(sol1.isUgly(1))
print(sol1.isUgly(14))

#time - O(log to base2 n)
#space - O(1)
            
            
        