class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        diffLen = abs(len(num1)-len(num2))
        if len(num1) > len(num2):
            num2 = "0" * diffLen + num2
        else:
            num1 = "0" * diffLen + num1
        
        sum = 0
        carryover = 0    
        result = ""
        for i in range(len(num1)-1, -1, -1):
            sum = int(num1[i]) + int(num2[i]) + carryover
            digit = sum % 10
            carryover = int(sum/10)
            result = str(digit) + result
            
        if carryover > 0:
            result = str(carryover) + result
        return result
        

sol1 = Solution()
print(sol1.addStrings("1234", "12"))
print(sol1.addStrings("12", "1234"))
print(sol1.addStrings("1234", "1234"))
print(sol1.addStrings("99", "123434"))

#time - O(n)
#space - O(1)