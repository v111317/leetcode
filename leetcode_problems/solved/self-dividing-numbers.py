#https://leetcode.com/problems/self-dividing-numbers/description/

# A self-dividing number is a number that is divisible by every digit it contains.

# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.

# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].
from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        
        for num in range(left, right+1):
            digits = str(num)
            count = 0
            for digit in digits:
                if digit=="0" or num%int(digit)!=0:
                    break
                else:
                    count += 1
            if count==len(digits):
                result.append(num)
        return result

sol1 = Solution()
print(sol1.selfDividingNumbers(1, 22))
print(sol1.selfDividingNumbers(47, 85))
