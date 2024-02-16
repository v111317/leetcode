class Solution:
    def addDigits(self, num: int) -> int:
        sum = 0
        
        if num==0:
            return num
        
        while num!=0:
            sum += num%10
            num /= 10
            num = int(num)
            if num==0:
                if sum%10==sum:
                    return sum
                else:
                    num = sum
                    sum = 0
                    
    def addDigits2(self, num: int) -> int:
        if num==0:
            return 0
        if num%9==0:
            return 9
        else:
            return num%9
        
sol1 = Solution()
print(sol1.addDigits(38))