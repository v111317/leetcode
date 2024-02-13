class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        diff = abs(len(a) - len(b)) 
        if len(a) > len(b):
            b = "0" * diff + b
        else:
            a = "0" * diff + a
        
        sum = ""    
        carryover = 0
        for i in range(len(a)-1, -1, -1):
            
            digitSum = int(a[i]) + int(b[i]) + carryover
            
            digit = 0
            match digitSum:
                case 1:
                    digit = 1
                    carryover = 0
                case 2:
                    digit = 0
                    carryover = 1
                case 3:
                    digit = 1
                    carryover = 1
            sum = str(digit) + sum
            
        if carryover == 1:
            sum = "1" + sum 
        return sum
            
            

#sol1 = Solution()
#sol1.addBinary("111", "10101")   
#sol1.addBinary("11010", "111") 
#time - O(n)
#space - O(1)       