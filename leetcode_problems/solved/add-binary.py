#Given two binary strings a and b, return their sum as a binary string.
#https://leetcode.com/problems/add-binary/description/

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
     
    def addBinary2(self, a: str, b: str) -> str:       
        num1 = int(a, 2)
        num2 = int(b, 2)
        sum = num1 + num2
        return bin(num1+num2)[2:] 
            

sol1 = Solution()
print(sol1.addBinary2("111", "10101"))
print(sol1.addBinary2("11010", "111"))


#Solution 1
#time - O(n)
#space - O(1)       

#Solution 2
#time - O(1)
#space - O(1)       