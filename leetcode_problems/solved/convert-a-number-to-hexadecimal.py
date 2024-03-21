#https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/

# Given an integer num, return a string representing its hexadecimal representation. 
# For negative integers, two’s complement method is used.

# All the letters in the answer string should be lowercase characters, and there should not be 
# any leading zeros in the answer except for the zero itself.

# Note: You are not allowed to use any built-in library method to directly solve this problem.

class Solution:
    def toHex(self, num: int) -> str:
        result = []
        base = 16
        numMap = {
            10: 'a',
            11: 'b',
            12: 'c',
            13: 'd',
            14: 'e',
            15: 'f'
        }
        
        if num < 0:
            num = (1 << 32) + num
        
        while num > 15:
            quotient = num // base
            remainder = num % base
            if remainder >= 10:
                remainder = numMap[remainder]
            result.insert(0, str(remainder))
            num = quotient
        if num >=10:
            num = numMap[num]
            
        result.insert(0, str(num))
        
        return "".join(result)
    
sol1 = Solution()
# print(sol1.toHex(26))
# print(sol1.toHex(95))
# print(sol1.toHex(253))
print(sol1.toHex(-3))
print(sol1.toHex(-1))
               