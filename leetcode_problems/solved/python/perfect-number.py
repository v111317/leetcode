#https://leetcode.com/problems/perfect-number/description/

# A perfect number is a positive integer that is equal to the sum of its positive divisors,
# excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

# Given an integer n, return true if n is a perfect number, otherwise return false.

class Solution:
    #Time Limit Exceeded
    def checkPerfectNumber(self, num: int) -> bool:
        numMap = {}
        count = 0
        for factor in range(1, num):
            if num%factor==0:
                quotient = int(num/factor)
                if quotient not in numMap:
                    numMap[quotient] = 1
                    numMap[factor] = 1
                    count += factor
                    
                    if quotient != num:
                        count += quotient
                else:
                    break
                            
        if count==num:
            return True
        else:
            return False

sol1 = Solution()
print(sol1.checkPerfectNumber(28))
print(sol1.checkPerfectNumber(7))
        
#time - O(n)
#space - O(n)