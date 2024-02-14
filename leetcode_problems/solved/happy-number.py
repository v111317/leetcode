class Solution:
    def isHappy(self, n: int) -> bool:
        
        squareMap = {}
        while n!=1:
            
            if n in squareMap:
                return False
            else:
                squareMap[n] = 1
            
            sum = 0
            while n!=0:
                sum += pow(n%10,2)
                n = int(n/10)
                
            if n==1:
                return True
            
            n = sum
            print(n)
        
        if n==1:
            return True

sol1 = Solution()
#print(sol1.isHappy(19)) 
print(sol1.isHappy(2))    
        