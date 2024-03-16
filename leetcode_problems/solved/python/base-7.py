#https://leetcode.com/problems/base-7/description/

#Given an integer num, return a string of its base 7 representation.

class Solution:
    def convertToBase7(self, num: int) -> str:
        result = []
        isNeg = False
        if num < 0:
            num = abs(num)
            isNeg = True
        while num >= 7:
            quotient = num//7
            remainder = num % 7
            result.insert(0, str(remainder))
            num = quotient
        result.insert(0, str(num))
        if isNeg:
            result.insert(0, "-")
        return "".join(result)

sol1 = Solution()
print(sol1.convertToBase7(100))
print(sol1.convertToBase7(-7))